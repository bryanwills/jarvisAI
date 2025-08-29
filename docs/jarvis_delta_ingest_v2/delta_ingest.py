#!/usr/bin/env python3
"""
delta_ingest.py
Incremental ("delta") ingester for RAG.

- Scans configured folders for text-like files.
- Tracks file state in a local SQLite database (path, size, mtime, sha256).
- Only sends changed/new files to the ingestion API (FastAPI at /ingest).
- Supports cadences (hot|warm|cold) to be run by different cron schedules.

Usage:
  python delta_ingest.py --config ingest.yaml --profile hot
  python delta_ingest.py --config ingest.yaml --profile warm
  python delta_ingest.py --config ingest.yaml --profile cold

Env:
  INGEST_API_URL  (default: http://localhost:8001/ingest)
  MAX_BYTES       (default: 20_000_000)  # skip bigger files unless overridden per-source
"""

import argparse
import os
import sys
import time
import hashlib
import sqlite3
from pathlib import Path
import fnmatch
import requests

DEFAULT_API = os.getenv("INGEST_API_URL", "http://localhost:8001/ingest")
DEFAULT_MAX = int(os.getenv("MAX_BYTES", "20000000"))  # 20MB

TEXT_EXTS = {
    ".md", ".mdx", ".txt", ".rst", ".markdown",
    ".py", ".js", ".ts", ".tsx", ".jsx", ".json", ".yaml", ".yml", ".toml",
    ".sh", ".bash", ".zsh", ".ps1", ".go", ".rs", ".java", ".kt", ".swift", ".rb", ".php", ".c", ".cpp", ".h", ".hpp",
    ".sql", ".ipynb"
}

def sha256_file(p: Path, block_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        while True:
            b = f.read(block_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def load_yaml(path: str):
    try:
        import yaml
    except ImportError:
        print("[!] Please: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def open_state_db(db_path: Path):
    conn = sqlite3.connect(str(db_path))
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
            path TEXT PRIMARY KEY,
            size INTEGER,
            mtime REAL,
            sha256 TEXT,
            last_ingest_ts REAL
        )
        """
    )
    conn.execute("CREATE INDEX IF NOT EXISTS idx_files_mtime ON files(mtime)")
    return conn

def should_include(p: Path, allow_exts, include_globs, exclude_globs) -> bool:
    if allow_exts and p.suffix.lower() not in allow_exts:
        return False
    s = str(p)
    if exclude_globs:
        for g in exclude_globs:
            if fnmatch.fnmatch(s, g):
                return False
    if include_globs:
        for g in include_globs:
            if fnmatch.fnmatch(s, g):
                return True
        return False
    return True

def iter_files(root: Path):
    for base, dirs, files in os.walk(root):
        for fn in files:
            yield Path(base) / fn

def read_text_file(p: Path, max_bytes: int):
    if p.stat().st_size > max_bytes:
        return None
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        try:
            return p.read_text(encoding="latin-1", errors="ignore")
        except Exception:
            return None

def ingest_one(api: str, path_str: str, text: str, type_: str, tags, privacy: str, source: str, metadata: dict):
    payload = {
        "path": path_str,
        "text": text,
        "type": type_,
        "tags": tags,
        "privacy": privacy,
        "source": source,
        "metadata": metadata or {},
    }
    r = requests.post(api, json=payload, timeout=120)
    r.raise_for_status()
    return r.json()

def run_profile(cfg: dict, profile: str):
    api = cfg.get("ingestion_api", DEFAULT_API)
    db_path = Path(cfg.get("state_db", "./delta_state.db")).resolve()
    conn = open_state_db(db_path)
    cur = conn.cursor()

    sources = [s for s in cfg.get("sources", []) if s.get("cadence", "hot") == profile]
    now = time.time()
    sent = 0
    skipped = 0

    for src in sources:
        root = Path(src["root"]).expanduser().resolve()
        if not root.exists():
            print(f"[!] Missing root: {root}")
            continue
        allow_exts = set([e.lower() for e in src.get("allow_exts", list(TEXT_EXTS))])
        include_globs = src.get("include_globs")
        exclude_globs = src.get("exclude_globs")
        max_bytes = int(src.get("max_bytes", DEFAULT_MAX))
        type_ = src.get("type", "file")
        tags = src.get("tags", [])
        privacy = src.get("privacy", "private")
        source = src.get("source", "vault")

        for p in iter_files(root):
            if not should_include(p, allow_exts, include_globs, exclude_globs):
                continue
            try:
                st = p.stat()
            except FileNotFoundError:
                continue

            row = cur.execute("SELECT size, mtime, sha256 FROM files WHERE path=?", (str(p),)).fetchone()
            size_changed = (row is None) or (row[0] != st.st_size)
            mtime_changed = (row is None) or (abs(row[1] - st.st_mtime) > 1e-6)
            need_hash = size_changed or mtime_changed
            sha = row[2] if (row and not need_hash) else sha256_file(p)

            if row and (row[2] == sha):
                skipped += 1
                continue

            text = read_text_file(p, max_bytes)
            if text is None or not text.strip():
                skipped += 1
                continue

            meta = {"path": str(p), "size": st.st_size, "mtime": st.st_mtime}
            try:
                resp = ingest_one(api, str(p), text, type_, tags, privacy, source, meta)
                sent += 1
                cur.execute(
                    "REPLACE INTO files(path,size,mtime,sha256,last_ingest_ts) VALUES(?,?,?,?,?)",
                    (str(p), st.st_size, st.st_mtime, sha, now),
                )
                conn.commit()
                print(f"[+] Ingested {p} -> {resp}")
            except Exception as e:
                print(f"[!] Failed ingest {p}: {e}")

    print(f"[done] profile={profile} sent={sent} skipped={skipped} state_db={db_path}")
    conn.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", required=True, help="YAML config path")
    ap.add_argument("--profile", required=True, choices=["hot", "warm", "cold"], help="Which cadence to run")
    args = ap.parse_args()

    cfg = load_yaml(args.config)
    run_profile(cfg, args.profile)

if __name__ == "__main__":
    main()
