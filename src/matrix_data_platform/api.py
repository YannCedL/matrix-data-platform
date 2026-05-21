from fastapi import FastAPI
from genesis_core import ResultContract
from .monitor import pipeline_status

app = FastAPI(title="Matrix Data Platform API", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Matrix"}

@app.get("/api/v1/pipelines", response_model=ResultContract)
def pipelines():
    return pipeline_status()
