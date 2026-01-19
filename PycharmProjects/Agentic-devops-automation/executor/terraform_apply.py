import subprocess
from pathlib import Path

def terraform_apply(tf_dir: Path):
    cmd = [
        "docker", "run", "--rm",
        "-v", f"{tf_dir.resolve()}:/workspace",
        "-w", "/workspace",
        "tf-sandbox",
        "apply", "-input=false", "tfplan"
    ]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return {
        "ok": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr
    }
