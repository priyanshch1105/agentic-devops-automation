from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "priyanshch1105/agentic-devops-automation"   # e.g. priyansh/agentic-devops
WORKFLOW_FILE = "terraform-gitops.yml"

class RunRequest(BaseModel):
    environment: str

@app.post("/run")
def run_workflow(req: RunRequest):
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "ref": "main",
        "inputs": {
            "environment": req.environment
        }
    }

    r = requests.post(url, headers=headers, json=payload)

    if r.status_code != 204:
        return {"error": r.text}

    return {"message": f"{req.environment} workflow triggered"}
