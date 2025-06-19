import asyncio
import os
from typing import Optional
from contextlib import AsyncExitStack
from google import genai
from google.genai import types
import json

from mcp import ClientSession
from mcp.client.sse import sse_client

from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env

api_key = os.getenv("GEMINI_API_KEY")

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.gemini = genai.Client(api_key=api_key)

    async def connect_to_sse_server(self, server_url: str):
        """Connect to an MCP server running with SSE transport"""
        # Store the context managers so they stay alive
        self._streams_context = sse_client(url=server_url)
        streams = await self._streams_context.__aenter__()

        self._session_context = ClientSession(*streams)
        self.session: ClientSession = await self._session_context.__aenter__()

        # Initialize
        await self.session.initialize()

        self.session.set_logging_level("info")

        # List available tools to verify connection
        print("Initialized SSE client...")
        print("Listing tools...")
        response = await self.session.list_tools()
        tools = response.tools
        print("\nConnected to server with tools:", [tool.name for tool in tools])

    async def cleanup(self):
        """Properly clean up the session and streams"""
        if self._session_context:
            await self._session_context.__aexit__(None, None, None)
        if self._streams_context:
            await self._streams_context.__aexit__(None, None, None)

    async def process_query(self, query: str) -> str:
        """Process a query using Claude and available tools"""
        
        response = await self.session.list_tools()
        available_tools = [{ 
            "name": tool.name,
            "description": tool.description,
            "input_schema": tool.inputSchema
        } for tool in response.tools]
        system_prompt = """You are a helpful assistant of select tools.
            Retorne no formado json valido para utilizar no python com o json.load(). não colocar ` nem a palavra json.
            Exemplo: '[{"type":"use_tool","tool_name":"add","tool_input":{"a":1,"b":1}},{"type":"text", "text":"O resultado é 2"}]'
            Obs: o resultado precisa ser sem as aspas simples.
        """
        messages = [{
            "role": "user",
            "content": query
        }]
        contentLLM = {
            "system_prompt": system_prompt,
            "messages": messages,
            "tools": available_tools
        }

        # Initial Claude API call
        # response = self.gemini.messages.create(
        #     model="claude-3-5-sonnet-20241022",
        #     max_tokens=1000,
        #     messages=messages,
        #     tools=available_tools
        # )
        response = self.gemini.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=str(contentLLM),
        )

        # Process response and handle tool calls
        tool_results = []
        final_text = []


        print(response.text)
        text_value = response.text.replace("```", "").replace("json", "")

        actions = json.loads(text_value)

        for action in actions:
            if action["type"] == 'text':
                final_text.append(action["text"])
            elif action["type"] == 'use_tool':
                tool_name = action["tool_name"]
                tool_args = action["tool_input"]
                
                # Execute tool call
                result = await self.session.call_tool(tool_name, tool_args)
                tool_results.append({"call": tool_name, "result": result})
                final_text.append(f"[Calling tool {tool_name} with args {tool_args}]")

                messages
                # Continue conversation with tool results
                if hasattr(action, 'text') and action["text"]:
                    messages.append({
                        "role": "assistant",
                        "content": action["text"]
                    })
                messages.append({
                    "role": "tool", 
                    "content": f"Result Tool {tool_name}: {str(result.content)}"
                })

        response = self.gemini.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=str(messages),
        )

        final_text.append(response.text)

        return "\n".join(final_text)
    

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")
        
        while True:
            try:
                query = input("\nQuery: ").strip()
                
                if query.lower() == 'quit':
                    break
                    
                response = await self.process_query(query)
                print("\n" + response)
                    
            except Exception as e:
                print(f"\nError: {str(e)}")


async def main():
    server_url = 'http://localhost:5005/sse'

    if len(sys.argv) >=2:
        server_url = sys.argv[1]

    client = MCPClient()
    try:
        await client.connect_to_sse_server(server_url=server_url)
        await client.chat_loop()
    finally:
        await client.cleanup()


if __name__ == "__main__":
    import sys
    asyncio.run(main())