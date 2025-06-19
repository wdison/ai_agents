import asyncio
from mcp.server.fastmcp import FastMCP, Context # FAST MCP is just an easier way to build a server

import logging
from tools_agents import add, divide, multiply, subtract

logging.basicConfig(level=logging.DEBUG)

# Create an MCP server named "Greeter"
print("MCP Server to Greeter")

mcp = FastMCP(name="Greeter", instructions=None,
        host="0.0.0.0",
        port="5005",
        log_level="DEBUG"
    )

@mcp.tool()
def greet(ctx: Context) -> str:
    """Return this welcome message, when greeted with "Hi", "Hey" or "Hello"."""
    print("-> Calling greet")
    ctx.log(level="info", message="Ola, com custom send log")
    return "Hey Wdison, Welcome to the world of MCPs!"

mcp.add_tool(add)
mcp.add_tool(subtract)
mcp.add_tool(multiply)
mcp.add_tool(divide)

if __name__ == "__main__":

    async def list_tools() -> None:
        print("List tools", await mcp.list_tools())
    try:
        asyncio.run(list_tools())
    except Exception as e:
        print(e)
    
    def run_server_assync():
        print("Starting server...")
        mcp.run(transport="sse")
        print("Server started!")

    run_server_assync()
    print("Server started 2!")