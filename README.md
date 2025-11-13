# IDCS-MCP

A MCP (Model Context Protocol) server that connects LLM agents to Oracle IDCS (Identity Cloud Service) APIs.
It converts Oracle's Swagger spec into MCP tools, letting agents manage identity operations through natural language.

### Features
- Auto-generates Python functions from Oracle IDCS OpenAPI specs
- Exposes IDCS operations as MCP tools (users, groups, apps, OAuth, SAML, SCIM)
- Handles OAuth2 authentication and token refresh
- Built-in validation and error handling
- Works with Claude Desktop, Cline, and custom MCP clients

[![IDCS-MCP Demo](https://img.youtube.com/vi/JGFJ8Xo8UyU/0.jpg)](https://www.youtube.com/watch?v=JGFJ8Xo8UyU)

### How it works
- Parses IDCS Swagger JSON into FastAPI routes
- FastMCP registers these as callable tools for LLM agents
- Agents invoke tools like `idcs.getUser` or `idcs.createGroup` via natural language
- Server executes API calls against Oracle IDCS with proper auth
- Enables complex workflows (user provisioning, MFA resets, OAuth config) through conversation


### Future
- Kubernetes/Docker deployment templates
- Role-based access control for tool invocation
- Response caching to reduce API calls
- SCIM event streaming as MCP resources
- Prebuilt prompt packs for enterprise workflows


### Build and Run
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

### How to run using MCP Host

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

### Contribution

Open issue and raise PR

### License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.