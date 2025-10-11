#!/usr/bin/env python3

import asyncio
import json
import sys
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import mansnip

app = Server("manpage-query")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="manpage_query",
            description="return a contextual snippet from a manpage",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": "man page section if needed for disambiguation"
                    },
                    "manpage": {
                        "type": "string",
                        "description": "man page to retrieve"
                    },
                    "query": {
                        "type": "string",
                        "description": "term to look up"
                    }
                },
                "required": ["manpage", "query"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "manpage_query":
        section = arguments.get("section") or ""
        page = arguments.get("manpage")
        query = arguments.get("query")
        res = mansnip.mansnip(section, page, query, {'MANSNIP_LLM': 1})
        return [TextContent(type="text", text=res)]
    
    raise ValueError(f"Unknown tool: {name}")

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
