# IDCS-MCP


## Build and Run Test

Clone the repo:
`git clone ssh://git@bitbucket.oci.oraclecorp.com:7999/~niledas/idcs-mcp.git`

Install uv and do uv sync:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
```

Running server using streamable-http:
`uv run src/server.py`

Running tests:
`uv run src/test.py`

## How to run using MCP Host

We are using Claude Desktop as the MCP Host, which provides easy way to connect to MCP Server using Connectors

Download Claude Desktop and signup/login: `https://claude.ai/download`

Connect to MCP server using below `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "idcs-mcp": {
      "command": "uv",
      "args": [
      	"run",
        "src/server.py"
      ],
      "cwd": "/home/user/MCP/idcs-mcp"
    }
  }
}
```

Restart Claude Desktop and you'll see MCP server context under prompt tools.

## How to contribute

Open Issue and PR Fix

## License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.