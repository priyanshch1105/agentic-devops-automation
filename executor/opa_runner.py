import json
import subprocess
from pathlib import Path
import shutil

OPA_BIN = shutil.which("opa")
if not OPA_BIN:
    raise RuntimeError("OPA binary not found in PATH")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
POLICIES_DIR = PROJECT_ROOT / "policies"

def run_opa(plan_json: Path) -> dict:
    if not plan_json.exists():
        raise FileNotFoundError(f"plan.json not found: {plan_json}")

    cmd = [
        OPA_BIN, "eval",
        "--format", "json",
        "--data", str(POLICIES_DIR),
        "--input", str(plan_json),
        "data.terraform.policy.deny"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"OPA runtime error\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    output = json.loads(result.stdout)
    violations = output["result"][0]["expressions"][0]["value"]

    return {
        "passed": len(violations) == 0,
        "violations": violations
    }
