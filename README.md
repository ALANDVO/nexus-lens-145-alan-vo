# Nexus Lens

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Official, Anthropic-managed directory of high quality Claude Code Plugins.

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm or pnpm

### Backend Setup
```bash
cd backend
pip install -e ".[dev]"
uvicorn main:app --reload --port 8000
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:3000 (proxied to backend at http://localhost:8000).

## Project Structure
```
nexus-lens/
├── backend/           # FastAPI application
│   └── main.py        # API endpoints
├── frontend/          # React + Vite application
│   └── src/
│       ├── App.tsx    # Main component
│       └── main.tsx   # Entry point
├── marketplace.json   # Plugin registry
├── plugins/           # Plugin source directories
├── pyproject.toml     # Python dependencies
└── feature-plan.json  # Implementation roadmap
```

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/marketplace` - List all plugins
- `GET /api/plugins/{plugin_id}` - Get plugin details

## Marketplace Schema

The `marketplace.json` follows the [Claude Plugin Marketplace schema](https://json.schemastore.org/claude-plugin-marketplace.json).

Each plugin entry includes:
- `id` - Unique identifier
- `name` - Display name
- `description` - Plugin description
- `version` - Semantic version
- `author` - Author name
- `repository` - Source code URL
- `license` - SPDX license identifier
- `keywords` - Search tags
- `source` - Relative path to plugin source
- `lspServers` - LSP server configuration (optional)

## Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests (when added)
cd frontend
npm test
```

### Linting
```bash
# Python
ruff check backend/

# TypeScript
cd frontend
npx tsc --noEmit
```

## License

Apache-2.0 - see LICENSE file for details.

Maintainer: Alan Vo <alanvo@gmail.com>
