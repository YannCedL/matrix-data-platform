import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .monitor import pipeline_status

app = FastAPI(
    title="Matrix Data Platform API",
    description="Plateforme d'Ingestion Centralisée & Supervision de Pipelines OSINT",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil de supervision d'ingestion
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Matrix API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "platform": "Matrix", "version": "1.0.0"}

@app.get("/api/v1/status", response_model=ResultContract)
def get_status():
    return pipeline_status()
