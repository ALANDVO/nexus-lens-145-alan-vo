# Changelog

## 1.1.0 — work-in-progress checkpoint

Partial code published for continued development. Known issues: STATUS.md.

All notable changes to this project will be documented in this format.

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
