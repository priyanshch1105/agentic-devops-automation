import subprocess
from pathlib import Path

def terraform_plan_json(tf_dir: Path) -> Path:
    # init
    subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{tf_dir.resolve()}:/workspace",
            "-w", "/workspace",
            "tf-sandbox",
            "init", "-input=false"
        ],
        check=True
    )

    # plan
    subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{tf_dir.resolve()}:/workspace",
            "-w", "/workspace",
            "tf-sandbox",
            "plan", "-out=tfplan"
        ],
        check=True
    )

    # show (capture stdout)
    result = subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{tf_dir.resolve()}:/workspace",
            "-w", "/workspace",
            "tf-sandbox",
            "show", "-json", "tfplan"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    plan_path = tf_dir / "plan.json"
    plan_path.write_text(result.stdout)

    return plan_path
