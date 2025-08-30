from server.core.schema import Decision, Citation
def test_decision_valid():
    Decision(
        decision="compliant",
        confidence=0.9,
        risk_score=0.1,
        rationale="All good.",
        citations=[Citation(doc_id="p1", chunk_id="1", snippet="abc")],
        open_questions=["None"],
        human_interactions=[]
    )
