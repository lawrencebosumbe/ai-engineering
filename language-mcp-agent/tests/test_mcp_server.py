import pytest

from mcp import Client

from app.mcp.language_server import mcp


@pytest.mark.anyio
async def test_list_tools():
    async with Client(mcp) as client:
        result = await client.list_tools()

        tool_names = {
            tool.name
            for tool in result.tools
        }

        assert "detect_text_language" in tool_names
        assert "extract_text_entities" in tool_names
        assert "detect_personal_information" in tool_names


@pytest.mark.anyio
async def test_language_tool():
    async with Client(mcp) as client:
        result = await client.call_tool(
            "detect_text_language",
            {
                "text": "This is an English sentence."
            }
        )

        assert result.structured_content["result"]["language"] == "en"