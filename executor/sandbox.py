import subprocess
from pathlib import Path

def run_terraform_plan(tf_dir: Path):
    cmd = [
        "docker", "run", "--rm",
        "-v", f"{tf_dir.absolute()}:/workspace",
        "hashicorp/terraform:1.7",
        "plan"
    ]

    result = subprocess.run(
        cmd, capture_output=True, text=True
    )

    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }
