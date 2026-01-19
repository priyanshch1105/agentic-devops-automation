import json
from pathlib import Path

def load_tfplan_json(tf_dir: Path) -> dict:
    plan_file = tf_dir / "plan.json"
    if not plan_file.exists():
        raise FileNotFoundError("plan.json not found. Run terraform show first.")

    return json.loads(plan_file.read_text())
