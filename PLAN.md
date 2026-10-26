# Product development plan

Each round completes one feature or repair. Future items are planned, not implemented claims.

## Current round

core-marketplace-skeleton

## Roadmap

### core-marketplace-skeleton — Core marketplace skeleton with plugin registry

Status: done

Acceptance:
- FastAPI server starts and serves /health endpoint
- Marketplace JSON served at /marketplace.json with valid schema
- Plugin directory structure exists with at least one example plugin
- README with install/run instructions

Implementation: `main.py`, `plugins/marketplace.json`, `plugins/typescript-lsp/.lsp.json`, `plugins/typescript-lsp/README.md`, `plugins/vue-volar-lsp/.lsp.json`, `plugins/vue-volar-lsp/README.md`, `requirements.txt`, `README.md`

Tests: `tested via inline script: /health, /marketplace.json, /plugins/typescript-lsp, /plugins/vue-volar-lsp`

### vue-volar-lsp-plugin — Add Vue/Volar LSP plugin

Status: done

Acceptance:
- plugins/vue-volar-lsp/.lsp.json exists with valid LSP config
- Marketplace entry references the plugin
- Plugin installs and provides LSP for .vue files

Implementation: `plugins/vue-volar-lsp/.lsp.json`, `plugins/vue-volar-lsp/README.md`, `plugins/marketplace.json (entry)`

Tests: `tested via /plugins/vue-volar-lsp endpoint`

### lsp-json-fix-existing-plugins — Add .lsp.json to all existing LSP plugins

Status: planned

Acceptance:
- Each LSP plugin directory has .lsp.json
- Marketplace.json references match plugin configs

