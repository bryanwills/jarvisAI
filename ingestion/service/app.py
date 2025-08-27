import os
import hashlib
from fastapi import FastAPI, Body
import psycopg2
from psycopg2.extras import Json
from sentence_transformers import SentenceTransformer

PGHOST = os.getenv("PGHOST", "db")
PGUSER = os.getenv("PGUSER", "jarvis")
PGPASSWORD = os.getenv("PGPASSWORD", "change-me")
PGDATABASE = os.getenv("PGDATABASE", "jarvis")
PGPORT = int(os.getenv("PGPORT", "5432"))
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "nomic-ai/nomic-embed-text-v1")

app = FastAPI(title="Jarvis Ingestion API")

_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model

def get_db():
    return psycopg2.connect(
        host=PGHOST,
        user=PGUSER,
        password=PGPASSWORD,
        dbname=PGDATABASE,
        port=PGPORT,
    )

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ingest")
def ingest(payload: dict = Body(...)):
    """
    payload: {
      "path": "...", "text": "...", "type": "file|note|code",
      "tags": ["notes","project-x"], "privacy": "private|public",
      "source": "vault|github|ocr", "metadata": {...}
    }
    """
    text = payload.get("text", "")
    if not text.strip():
        return {"ok": False, "error": "empty text"}

    # naive chunking
    chunk_size = 2000
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = get_model().encode(chunks).tolist()

    with get_db() as conn:
        with conn.cursor() as cur:
            doc_hash = hashlib.sha256(text.encode()).hexdigest()
            cur.execute(
                """
                INSERT INTO documents(path, type, tags, privacy, source, hash, text)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id
                """,
                (
                    payload.get("path"),
                    payload.get("type"),
                    payload.get("tags"),
                    payload.get("privacy"),
                    payload.get("source"),
                    doc_hash,
                    text,
                ),
            )
            doc_id = cur.fetchone()[0]

            for idx, (chunk_text, vec) in enumerate(zip(chunks, embeddings)):
                cur.execute(
                    """
                    INSERT INTO chunks(document_id, chunk_idx, text, embedding, metadata)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (
                        doc_id,
                        idx,
                        chunk_text,
                        vec,
                        Json(payload.get("metadata") or {"path": payload.get("path")}),
                    ),
                )

    return {"ok": True, "doc_id": doc_id, "chunks": len(chunks)}
