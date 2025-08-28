# Step 6 — Embeddings Service (Local)
**Goal:** A small API to embed chunks and upsert to Postgres.

## Option A: Python + sentence-transformers/nomic-embed
- Pros: flexible, GPU optional.  
- Cons: slightly more setup.

## Sample FastAPI service
```python
from fastapi import FastAPI, Body
import psycopg2, os, hashlib, json
from sentence_transformers import SentenceTransformer

app = FastAPI()
emb = SentenceTransformer('nomic-ai/nomic-embed-text-v1')  # or local model path

def db():
    return psycopg2.connect(
        host=os.getenv("PGHOST","db"),
        user=os.getenv("PGUSER","jarvis"),
        password=os.getenv("PGPASSWORD","change-me"),
        dbname=os.getenv("PGDATABASE","jarvis")
    )

@app.post("/ingest")
def ingest(payload=Body(...)):
    # payload: {path, text, type, tags[], privacy, source}
    text = payload["text"]
    chunks = [text[i:i+2000] for i in range(0,len(text),2000)]
    vecs = emb.encode(chunks).tolist()
    with db() as conn, conn.cursor() as cur:
        h = hashlib.sha256(text.encode()).hexdigest()
        cur.execute(
            "INSERT INTO documents(path,type,tags,privacy,source,hash,text) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING id",
            (payload["path"], payload.get("type"), payload.get("tags"),
             payload.get("privacy"), payload.get("source"), h, text)
        )
        doc_id = cur.fetchone()[0]
        for i,(c,v) in enumerate(zip(chunks,vecs)):
            cur.execute(
                "INSERT INTO chunks(document_id,chunk_idx,text,embedding,metadata) VALUES(%s,%s,%s,%s,%s)",
                (doc_id, i, c, v, json.dumps({"path": payload["path"]}))
            )
    return {"ok": True}
```

## Compose (add to stack)
Expose on `http://ingest.local:8001` behind reverse proxy.
