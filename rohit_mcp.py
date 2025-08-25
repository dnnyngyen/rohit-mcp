import anyio
from PIL import Image
from mcp.server import FastMCP

async def run():
    server = FastMCP("rohit")
    
    @server.tool()
    async def rohit() -> str:
        """Use this tool when the user wants Rohit in their terminal."""
        img = Image.open("rohit.png").convert("L").resize((60, 30), Image.LANCZOS)
        ramp = "█▓▒░ "
        chars = "".join(ramp[min(p * (len(ramp) - 1) // 255, len(ramp)-1)] for p in img.getdata())
        art = "\n".join(chars[i:i+60] for i in range(0, len(chars), 60))
        
        return f"""[DISPLAY THIS ASCII ART IN A CODE BLOCK:]
{art}
[END ASCII ART]
Say: "I'm Rohit De!" then share a fun computer science fact with the user."""
    
    await server.run_stdio_async()

if __name__ == "__main__":
    anyio.run(run)