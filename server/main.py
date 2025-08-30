from fastapi import FastAPI, WebSocket, UploadFile
from .core import dag, schema
from .agents import *
import uuid, asyncio, logging

app = FastAPI()
sessions = {}  # session_id -> websocket

@app.websocket("/connect")
async def connect(ws: WebSocket, session_id: str):
    await ws.accept()
    sessions[session_id] = ws
    while True:                         # keep connection open
        data = await ws.receive_json()
        # client HITL response
        ctx = store.load(session_id)
        ctx["human_responses"].append(data)
        store.save(session_id, ctx)

@app.post("/ask")
async def ask(question: str):
    session_id = str(uuid.uuid4())
    job_id = str(uuid.uuid4())
    ctx = {"query": question, "human_responses": []}
    store.save(session_id, ctx)
    asyncio.create_task(run_job(session_id, job_id))
    return {"session_id": session_id, "job_id": job_id}

async def run_job(session_id, job_id):
    ctx = store.load(session_id)
    g = dag.DAG([
        dag.Node("policy", policy_retriever.run),
        dag.Node("evidence", evidence_collector.run),
        dag.Node("vision", vision_agent.run),
        dag.Node("code", code_scanner.run),
        dag.Node("risk", risk_scorer.run),
        dag.Node("critic", red_team_critic.run)
    ])
    # dependencies
    g.nodes["risk"].deps = ["policy", "evidence", "vision", "code"]
    g.nodes["critic"].deps = ["risk"]

    results = await g.execute(ctx)
    decision = schema.Decision(
        decision="insufficient_evidence" if ctx["open_questions"] else "compliant",
        confidence=1.0 - ctx["risk_score"],
        risk_score=ctx["risk_score"],
        rationale="Prototype rationale",
        citations=ctx["policy"] + ctx["evidence"],
        open_questions=ctx["open_questions"],
        human_interactions=[]
    )
    store.save_result(job_id, decision.dict())

@app.get("/result")
async def result(job_id: str):
    return store.load_result(job_id)
