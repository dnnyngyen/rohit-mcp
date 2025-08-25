# Rohit MCP

A super simple MCP (Model Context Protocol) server that demonstrates how easy it is to create custom tools in less than 30 lines of code.

## What it does

When you call the `rohit` tool, it:
1. Converts Rohit's photo to ASCII art
2. Returns it with a greeting and a fun CS fact

## Files

- `rohit_mcp.py` - The MCP server (24 lines of code!)
- `rohit.png` - Rohit's photo
- `requirements.txt` - Dependencies

## Quick start

```bash
pip install -r requirements.txt
python rohit_mcp.py
```

## Setup for any MCP client

Add this to your MCP client configuration (e.g., `~/.cursor/mcp.json` for Cursor):

```json
{
  "rohit": {
    "command": "python3",
    "args": ["/path/to/rohit_mcp/rohit_mcp.py"],
    "env": {}
  }
}
```

Replace `/path/to/rohit_mcp/` with the actual path to this repository on your system.
