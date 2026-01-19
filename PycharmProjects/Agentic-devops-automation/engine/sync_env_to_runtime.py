import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INFRA_DIR = PROJECT_ROOT / "infra"
RUNTIME_DIR = INFRA_DIR / "runtime"

def sync_env_to_runtime(env: str):
    src = INFRA_DIR / env
    if not src.exists():
        raise ValueError(f"Environment not found: {env}")

    if RUNTIME_DIR.exists():
        shutil.rmtree(RUNTIME_DIR)

    shutil.copytree(src, RUNTIME_DIR)
    return str(RUNTIME_DIR)
