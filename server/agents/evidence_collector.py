# server/agents/evidence_collector.py
"""
Collects concrete evidence from product documentation and specs.
Assumes docs are already embedded in a FAISS/Qdrant index called evidence_index.
"""

from sentence_transformers import SentenceTransformer
import faiss
import pickle, asyncio

# load once at module import
model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("indexes/evidence.index")
with open("indexes/evidence_meta.pkl", "rb") as f:
    meta = pickle.load(f)          # list[{doc_id, chunk_id, text}]

TOP_K = 4

async def run(context: dict):
    query = context["query"]
    embedding = model.encode([query])
    D, I = index.search(embedding, TOP_K)  # distances, indices
    chunks = [meta[i] for i in I[0]]
    # store for downstream agents
    context["evidence"] = chunks
    return chunks
