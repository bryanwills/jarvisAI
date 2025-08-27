-- Enable pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Create n8n database if not exists
DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'n8n') THEN
      PERFORM pg_sleep(0); -- placeholder; create manually if needed
   END IF;
END$$;

-- Core tables for RAG
CREATE TABLE IF NOT EXISTS documents (
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

CREATE TABLE IF NOT EXISTS chunks (
  id SERIAL PRIMARY KEY,
  document_id INT REFERENCES documents(id) ON DELETE CASCADE,
  chunk_idx INT,
  text TEXT,
  embedding vector(768),
  metadata JSONB
);

-- Vector index
CREATE INDEX IF NOT EXISTS chunks_embedding_idx ON chunks USING ivfflat (embedding vector_cosine_ops);
