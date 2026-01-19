from pathlib import Path
from executor.approval_store import get_plan
from executor.terraform_apply import terraform_apply

def apply_agent(plan_id: str, tf_dir: str):
    record = get_plan(plan_id)

    if record["status"] != "APPROVED":
        raise PermissionError("Plan not approved. Apply blocked.")

    result = terraform_apply(Path(tf_dir))

    return {
        "applied": result["ok"],
        "output": result["stdout"] if result["ok"] else result["stderr"]
    }
