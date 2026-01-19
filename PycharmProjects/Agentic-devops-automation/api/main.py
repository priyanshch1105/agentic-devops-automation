from fastapi import FastAPI
from api.routes import generate

app = FastAPI(
    title="Agentic DevOps Assistant",
    version="0.1.0"
)

app.include_router(generate.router, prefix="/generate", tags=["Generate"])

@app.get("/health")
def health():
    return {"status": "ok"}
