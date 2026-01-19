from pathlib import Path
import json
from executor.terraform_runner import terraform_plan_json
from executor.opa_runner import run_opa
from executor.plan_summary import summarize_plan
from executor.approval_store import save_pending

def verifier_agent(state: dict) -> dict:
    tf_dir = Path(state["tf_dir"])

    plan_json_path = terraform_plan_json(tf_dir)
    plan = json.loads(plan_json_path.read_text())

    opa = run_opa(plan_json_path)
    summary = summarize_plan(plan)

    status = "POLICY_VIOLATION" if not opa["passed"] else "PENDING_APPROVAL"
    plan_id = None
    if status == "PENDING_APPROVAL":
        plan_id = save_pending(plan_json_path, summary)

    return {
        **state,
        "status": status,
        "opa": opa,
        "summary": summary,
        "plan_id": plan_id
    }
