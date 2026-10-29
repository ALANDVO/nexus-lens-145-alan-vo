"""FastAPI application for Nexus Lens marketplace."""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import json

app = FastAPI(title="Nexus Lens Marketplace", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MARKETPLACE_PATH = Path(__file__).parent.parent / "marketplace.json"

def load_marketplace():
    if not MARKETPLACE_PATH.exists():
        return {"plugins": []}
    with open(MARKETPLACE_PATH) as f:
        return json.load(f)

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/marketplace")
async def get_marketplace():
    return load_marketplace()

@app.get("/api/plugins/{plugin_id}")
async def get_plugin(plugin_id: str):
    data = load_marketplace()
    for plugin in data.get("plugins", []):
        if plugin.get("id") == plugin_id:
            return plugin
    raise HTTPException(status_code=404, detail="Plugin not found")
