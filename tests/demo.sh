#!/bin/bash
curl -X POST "http://localhost:8000/ask?question=Does new login meet MFA?"
# note the job_id, then:
sleep 5
curl "http://localhost:8000/result?job_id=..."
