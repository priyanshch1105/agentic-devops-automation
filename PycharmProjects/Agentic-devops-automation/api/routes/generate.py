from fastapi import APIRouter
from devops_agents.orchestrator import run_orchestrator

router = APIRouter()

@router.post("/")
def generate(body: dict):
    return run_orchestrator(body["prompt"])
