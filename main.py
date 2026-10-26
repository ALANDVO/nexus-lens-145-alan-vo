from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI(title="Nexus Lens Marketplace", version="0.1.0")

PLUGINS_DIR = Path(__file__).parent / "plugins"
MARKETPLACE_JSON = PLUGINS_DIR / "marketplace.json"

class PluginSource(BaseModel):
    type: str = "git"
    url: str

class LSPServer(BaseModel):
    command: str
    args: list[str] = []
    transport: str = "stdio"
    initializationOptions: dict = {}

class MarketplacePlugin(BaseModel):
    name: str
    description: str
    version: str
    source: PluginSource
    lspServers: dict[str, LSPServer] = {}
    strict: bool = False

class Marketplace(BaseModel):
    schemaVersion: str = "1.0"
    plugins: list[MarketplacePlugin]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/marketplace.json")
async def marketplace():
    if MARKETPLACE_JSON.exists():
        with open(MARKETPLACE_JSON) as f:
            return JSONResponse(json.load(f))
    return JSONResponse({"schemaVersion": "1.0", "plugins": []})

@app.get("/plugins/{plugin_name}")
async def plugin_info(plugin_name: str):
    plugin_path = PLUGINS_DIR / plugin_name
    if not plugin_path.exists():
        return JSONResponse({"error": "Plugin not found"}, status_code=404)

    lsp_path = plugin_path / ".lsp.json"
    if lsp_path.exists():
        with open(lsp_path) as f:
            return JSONResponse(json.load(f))

    readme_path = plugin_path / "README.md"
    if readme_path.exists():
        return FileResponse(readme_path)

    return JSONResponse({"error": "No plugin config found"}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
