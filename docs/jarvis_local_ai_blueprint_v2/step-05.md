# Step 5 — Data Layer: Postgres + pgvector
**Goal:** Stand up the vector store + schema.

## Docker Compose
Create `deploy/compose/db.yml`:
```yaml
services:
  db:
    image: ankane/pgvector:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: change-me
      POSTGRES_DB: jarvis
      POSTGRES_USER: jarvis
    volumes:
      - dbdata:/var/lib/postgresql/data
    ports: ["5432:5432"]
volumes:
  dbdata:
```

## Schema (run once)
```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE documents (
  id SERIAL PRIMARY KEY,
  path TEXT,
  type TEXT,
  tags TEXT[],
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now(),
  privacy TEXT,
  source TEXT,
  hash TEXT,
  text TEXT
);

CREATE TABLE chunks (
  id SERIAL PRIMARY KEY,
  document_id INT REFERENCES documents(id) ON DELETE CASCADE,
  chunk_idx INT,
  text TEXT,
  embedding vector(768),
  metadata JSONB
);

CREATE INDEX ON chunks USING ivfflat (embedding vector_cosine_ops);

CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  ts TIMESTAMPTZ,
  kind TEXT,
  payload JSONB
);

CREATE TABLE summaries (
  id SERIAL PRIMARY KEY,
  day DATE,
  type TEXT,
  text TEXT,
  metrics JSONB
);
```
