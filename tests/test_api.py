"""Tests for the marketplace API."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac

@pytest.mark.asyncio
async def test_health_endpoint(client: AsyncClient):
    response = await client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
async def test_marketplace_endpoint(client: AsyncClient):
    response = await client.get("/api/marketplace")
    assert response.status_code == 200
    data = response.json()
    assert "plugins" in data
    assert isinstance(data["plugins"], list)
    assert len(data["plugins"]) >= 4  # We have 4 initial plugins

@pytest.mark.asyncio
async def test_marketplace_plugin_structure(client: AsyncClient):
    response = await client.get("/api/marketplace")
    data = response.json()
    for plugin in data["plugins"]:
        assert "id" in plugin
        assert "name" in plugin
        assert "description" in plugin
        assert "version" in plugin
        assert "author" in plugin
        assert "repository" in plugin
        assert "license" in plugin
        assert "keywords" in plugin
        assert "source" in plugin

@pytest.mark.asyncio
async def test_plugin_detail_endpoint(client: AsyncClient):
    response = await client.get("/api/plugins/typescript-lsp")
    assert response.status_code == 200
    plugin = response.json()
    assert plugin["id"] == "typescript-lsp"
    assert plugin["name"] == "TypeScript LSP"

@pytest.mark.asyncio
async def test_plugin_detail_not_found(client: AsyncClient):
    response = await client.get("/api/plugins/nonexistent")
    assert response.status_code == 404
