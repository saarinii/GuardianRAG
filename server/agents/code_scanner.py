# server/agents/code_scanner.py
"""
Scans supplied code/config snippets for patterns relevant to compliance policy.
Uses simple keyword heuristics for demo; can be upgraded to AST parsing or
regex rules.
"""

import re, asyncio

# quick regex patterns keyed by a descriptive tag
PATTERNS = {
    "mfa_enabled": re.compile(r"(?i)multifactor|2fa|otp|authenticator"),
    "password_complexity": re.compile(r"(?i)min_length\s*[:=]\s*(8|10|12)"),
    "encryption": re.compile(r"(?i)aes[-_ ]?(256|128)|encrypt"
                             r"|crypto\.createCipher")
}

async def run(context: dict):
    code_snips = context.get("code", [])          # list[str]
    hits = []
    for idx, code in enumerate(code_snips):
        for tag, rx in PATTERNS.items():
            if rx.search(code):
                hits.append({
                    "doc_id": f"code_{idx}",
                    "chunk_id": tag,
                    "snippet": code[:120] + "..."
                })
    context.setdefault("evidence", []).extend(hits)
    return hits
