# GuardianRAG

GuardianRAG is an **AI Compliance Orchestrator** designed to automate, evaluate, and coordinate compliance checks through multi-agent workflows.  
It uses a DAG-based execution engine, integrates with human-in-the-loop (HITL) systems, and supports both automated and interactive compliance evaluations.

---

## 📂 Project Structure

```
ai-compliance-orchestrator/
├── server/
│   ├── main.py        # FastAPI entrypoint
│   ├── agents/        # Autonomous agents for compliance tasks
│   │   ├── __init__.py
│   │   ├── policy_retriever.py   # Retrieves and parses compliance policies
│   │   ├── evidence_collector.py # Collects supporting compliance evidence
│   │   ├── vision_agent.py       # Handles vision-based inspections
│   │   ├── code_scanner.py       # Static code compliance scanner
│   │   ├── risk_scorer.py        # Assigns compliance risk scores
│   │   └── red_team_critic.py    # Adversarial critic for robustness
│   ├── core/
│   │   ├── dag.py     # Async DAG executor for orchestrating agents
│   │   ├── schema.py  # Pydantic models for strict JSON validation
│   │   └── storage.py # MongoDB + Redis persistence layer
│   ├── ws_manager.py  # WebSocket HITL manager
│   └── config.yaml    # Configuration file
├── client/
│   ├── hitl_cli.py    # CLI for Human-in-the-Loop responses
└── README.md
```
<img width="2400" height="1600" alt="image" src="https://github.com/user-attachments/assets/c5494464-e79a-4c57-925b-4e63d590a98b" />

<img width="2400" height="1600" alt="image" src="https://github.com/user-attachments/assets/14127ab3-6bd1-4f70-9a0b-5e82d4de06c6" />

---

## 🚀 Features

- **FastAPI Server** – Provides APIs for compliance orchestration.  
- **Multi-Agent System** – Includes retrievers, evidence collectors, risk scorers, and red-team critics.  
- **Async DAG Engine** – Executes workflows across agents in parallel.  
- **HITL Integration** – Supports interactive human decisions via WebSocket + CLI.  
- **Storage Layer** – MongoDB and Redis helpers for state and caching.  

---

## ⚡ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/GuardianRAG.git
cd GuardianRAG/ai-compliance-orchestrator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
uvicorn server.main:app --reload
```

### 4. Start HITL client (optional)
```bash
python client/hitl_cli.py
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **MongoDB**
- **Redis**
- **WebSockets**
- **Pydantic**

---

## 📌 Roadmap

- [ ] Add CI/CD pipelines  
- [ ] Extend policy retriever for multiple compliance frameworks  
- [ ] Integrate LLM-based red-teaming  
- [ ] Build web dashboard for monitoring  

---

## 📄 License

This project is licensed under the MIT License.
