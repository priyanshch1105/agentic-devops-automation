import subprocess
import json

def opa_evaluate(plan_json_path: str) -> dict:
    result = subprocess.run(
        [
            "opa", "eval",
            "--data", "policies",
            "--input", plan_json_path,
            "data.terraform.policy.deny"
        ],
        capture_output=True,
        text=True
    )

    violations = json.loads(result.stdout)["result"][0]["expressions"][0]["value"]

    return {
        "passed": len(violations) == 0,
        "violations": violations
    }
