# Nexus Lens Marketplace

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Official, Anthropic-managed directory of high quality Claude Code Plugins.

## Quick Start

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

The server will start on `http://localhost:8000`.

## Endpoints

- `GET /health` - Health check
- `GET /marketplace.json` - Full marketplace catalog
- `GET /plugins/{plugin_name}` - Plugin info (serves .lsp.json or README.md)

## Plugin Structure

```
plugins/
├── marketplace.json          # Marketplace catalog
├── typescript-lsp/
│   ├── .lsp.json            # LSP server configuration
│   └── README.md            # Plugin documentation
└── vue-volar-lsp/
    ├── .lsp.json            # LSP server configuration
    └── README.md            # Plugin documentation
```

## Adding Plugins

1. Create a directory under `plugins/` with the plugin name
2. Add `.lsp.json` with LSP server configuration
3. Add `README.md` with documentation
4. Add entry to `plugins/marketplace.json`

## LSP Configuration Format

```json
{
  "lspServers": {
    "language-id": {
      "command": "language-server-binary",
      "args": ["--stdio"],
      "transport": "stdio",
      "initializationOptions": {}
    }
  }
}
```

## License

Apache-2.0

Maintainer: Alan Vo <alanvo@gmail.com>
