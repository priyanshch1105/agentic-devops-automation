import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parents[1]
STORE = PROJECT_ROOT / "approvals"
STORE.mkdir(exist_ok=True)

def save_pending(plan_json: Path, summary: dict) -> str:
    ts = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    pid = f"plan_{ts}"
    data = {
        "id": pid,
        "status": "PENDING_APPROVAL",
        "summary": summary
    }
    (STORE / f"{pid}.json").write_text(json.dumps(data, indent=2))
    return pid

def update_status(plan_id: str, status: str):
    p = STORE / f"{plan_id}.json"
    if not p.exists():
        raise FileNotFoundError(f"Approval file not found: {p}")

    d = json.loads(p.read_text())
    d["status"] = status
    p.write_text(json.dumps(d, indent=2))
    
def get_plan(plan_id: str) -> dict:
    p = STORE / f"{plan_id}.json"
    if not p.exists():
        raise FileNotFoundError("Plan approval record not found")
    return json.loads(p.read_text())
