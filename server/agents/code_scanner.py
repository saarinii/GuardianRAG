async def run(context):
    """Retrieve top-k policy chunks with FAISS; return list[dict]."""
    query = context["query"]
    # TODO: embed query, search vector DB, fetch chunks
    return [{"doc_id": "policy123", "chunk_id": "7", "snippet": "MFA required."}]
