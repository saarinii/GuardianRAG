# server/agents/vision_agent.py
"""
Extracts text from any image attachments via OCR (pytesseract).
The extracted text is appended to the evidence pool.
"""

import pytesseract, io, base64, asyncio
from PIL import Image

async def _ocr_bytes(img_bytes: bytes) -> str:
    img = Image.open(io.BytesIO(img_bytes))
    text = pytesseract.image_to_string(img)
    return text

async def run(context: dict):
    ocr_chunks = []
    for i, att in enumerate(context.get("attachments", [])):
        if att["type"].startswith("image/"):
            # attachment["data"] is assumed base64 string
            img_bytes = base64.b64decode(att["data"])
            text = await _ocr_bytes(img_bytes)
            ocr_chunks.append({
                "doc_id": f"image_{i}",
                "chunk_id": "ocr",
                "snippet": text.strip()
            })
    # merge into evidence – create list if first agent to add
    context.setdefault("evidence", []).extend(ocr_chunks)
    return ocr_chunks
