from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import requests
import os

app = FastAPI(
    title="Agentic DevOps Backend",
    version="0.1.0"
)

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "priyanshch1105/agentic-devops-automation"
WORKFLOW_FILE = "terraform-gitops.yml"

if not GITHUB_TOKEN:
    raise RuntimeError("GITHUB_TOKEN is not set")

# ---- Request Schema (STRICT) ----
class RunRequest(BaseModel):
    environment: Literal["dev", "staging", "prod"]

# ---- Health Endpoint ----
@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Agentic DevOps Backend",
        "usage": "POST /run with { environment: dev | staging | prod }"
    }

# ---- Trigger Workflow ----
@app.post("/run")
def run_workflow(req: RunRequest):
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{WORKFLOW_FILE}/dispatches"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    payload = {
        "ref": "master",
        "inputs": {
            "environment": req.environment
        }
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 401:
        raise HTTPException(status_code=401, detail="Invalid GitHub token")

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Repository or workflow file not found"
        )

    if response.status_code != 204:
        raise HTTPException(
            status_code=500,
            detail=response.text
        )

    return {
        "message": f"{req.environment} workflow triggered successfully"
    }
