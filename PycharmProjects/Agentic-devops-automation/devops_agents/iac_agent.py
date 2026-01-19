from pathlib import Path

RUNTIME_DIR = Path("infra/runtime")

def iac_agent(state: dict) -> dict:
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)

    (RUNTIME_DIR / "main.tf").write_text("""
terraform {
  required_version = ">= 1.6.0"
}
""")

    return {
        **state,
        "tf_dir": str(RUNTIME_DIR)
    }
