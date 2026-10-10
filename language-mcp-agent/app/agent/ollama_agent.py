from ollama import chat
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


MODEL = "llama3.2"


def mcp_tool_to_ollama_tool(tool) -> dict:
    """Convert an MCP tool definition into Ollama's tool format."""
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description or "",
            "parameters": tool.input_schema,
        },
    }


async def run_agent(user_prompt: str) -> str:
    """Run the Ollama agent using tools exposed by the MCP server."""

    server_parameters = StdioServerParameters(
        command="python",
        args=["-m", "app.mcp.language_server"],
    )

    async with stdio_client(server_parameters) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:

            # 1. Initialize MCP connection
            await session.initialize()

            # 2. Discover available MCP tools
            tool_result = await session.list_tools()

            tools = [
                mcp_tool_to_ollama_tool(tool)
                for tool in tool_result.tools
            ]

            # 3. Send the user's request to Llama
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a text analysis agent. "
                        "Use the available tools when they are appropriate "
                        "to analyze language, entities, or personal information."
                    ),
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ]

            response = chat(
                model=MODEL,
                messages=messages,
                tools=tools,
            )

            # 4. Check whether Llama requested a tool
            if not response.message.tool_calls:
                return response.message.content

            # 5. Add Llama's tool-call message
            messages.append(response.message)

            # 6. Execute every requested MCP tool
            for tool_call in response.message.tool_calls:

                tool_name = tool_call.function.name
                arguments = tool_call.function.arguments

                result = await session.call_tool(
                    tool_name,
                    arguments,
                )

                # 7. Give the MCP result back to Llama
                messages.append(
                    {
                        "role": "tool",
                        "tool_name": tool_name,
                        "content": str(result.structured_content),
                    }
                )

            # 8. Ask Llama to produce the final response
            final_response = chat(
                model=MODEL,
                messages=messages,
            )

            return final_response.message.content


if __name__ == "__main__":
    import asyncio

    prompt = (
        "Analyze this text and identify its language, "
        "named entities, and any personal information: "
        "'John Smith works for Microsoft in London. "
        "His email is john.smith@example.com.'"
    )

    result = asyncio.run(run_agent(prompt))

    print("\nAgent response:\n")
    print(result)