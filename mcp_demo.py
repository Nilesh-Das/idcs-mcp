from fastmcp import FastMCP
from dotenv import load_dotenv

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def main():
    print("Hello from test!")

if __name__ == "__main__":
    mcp.run()
