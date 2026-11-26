# Changelog

## 1.6.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.5.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.4.1 — volar LSP plugin addition

### Added
- Volarlsp LSP plugin (issue #232):
  - plugins/volar-lsp/.lsp.json created
  - marketplace.json entry added with vue-language-server configuration
  - Backend API serves volar-lsp plugin detail correctly

### Verified
- All 5 API tests pass
- Plugin detail endpoint returns volar-lsp data correctly
- Frontend TypeScript compiles without errors

## 1.4.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.3.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.2.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

## 1.1.0 — work-in-progress checkpoint

### Added
- 7 additional LSP plugins to match official marketplace (11 total):
  - clangd-lsp (C/C++)
  - php-lsp (PHP via Intelephense)
  - swift-lsp (Swift via sourcekit-lsp)
  - kotlin-lsp (Kotlin via kotlin-language-server)
  - csharp-lsp (C# via csharp-ls)
  - jdtls-lsp (Java via JDTLS)
  - lua-lsp (Lua via lua-language-server)
- Each plugin has .lsp.json configuration file
- All 11 plugins registered in marketplace.json

### Verified
- Backend tests pass (5/5)
- Frontend builds successfully
- Backend linting passes (ruff)

Partial code published for continued development. Known issues: STATUS.md.

## [0.1.0] - 2026-10-25

### Added
- FastAPI backend with marketplace API endpoints
- React + Vite frontend with plugin list view
- Marketplace.json with 4 LSP plugins (TypeScript, Pyright, gopls, Rust Analyzer)
- Test suite with 5 passing tests
- README with install/run instructions
- Feature plan and status tracking

### Fixed
- Backend plugin detail endpoint returns proper 404 for missing plugins
- Package discovery configuration in pyproject.toml

### Infrastructure
- Python virtual environment setup
- Frontend build pipeline with TypeScript and Vite
- CORS configuration for local development

---

Alan Vo · [alanvo.net](https://alanvo.net) · [X: @alanvoasi](https://x.com/alanvoasi)
