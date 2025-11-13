#!/usr/bin/env python3
"""Command-line interface for FastMCP Tutorial Server."""

import argparse
from asyncio.log import logger
import sys

from fastmcp import Client
from src import mcp
from fastmcp.client.transports import StreamableHttpTransport


async def call_mcp_tool(url: str, tool_name: str, parameters: dict) -> dict:
    """Call a specific tool on the MCP server.

    Args:
        url (str): The base URL of the server.
        tool_name (str): The name of the tool to call.
        parameters (dict): The parameters to pass to the tool
    """

    logger.debug(f"Calling tool '{tool_name}' with parameters: {parameters}")

    # see if url is valid and there exists a tool with the given name
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("Invalid URL format. URL must start with 'http://' or 'https://'.")
    if not tool_name:
        raise ValueError("Tool name cannot be empty.")

    async with Client(transport=StreamableHttpTransport(url=url)) as client:
        tools = await client.list_tools()
        if any(tool.name == tool_name for tool in tools):
            result = await client.call_tool(tool_name, parameters)

            logger.debug(f"Tool '{tool_name}' called successfully. Result: {result}")
            return result
        else:
            raise ValueError(f"Tool '{tool_name}' not found on the server.")

    result = asyncio.run(call_mcp_tool(args.url, tool.name, {}))
    print(Pretty(result))

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="FastMCP Tutorial Server - A comprehensive MCP server example"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind to (default: localhost)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=3000,
        help="Port to bind to (default: 3000)"
    )
    
    args = parser.parse_args()
    
    print("Starting FastMCP Tutorial Server...")
    print(f"Tools: 3 | Resources: 4 | Prompts: 4")
    print("Press Ctrl+C to stop the server")
    
    try:
        mcp.run()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
