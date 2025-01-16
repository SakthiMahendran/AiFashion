from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
import uvicorn
from rich.console import Console
import time

app = FastAPI()
console = Console()

# Get the directory where the Python file is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Print the current script directory
console.print(f"[bold yellow]Current Directory:[/bold yellow] [underline blue]{script_directory}[/underline blue]")

# Serve the index.html file at /home
@app.get("/home")
async def serve_home():
    return FileResponse(os.path.join(script_directory, "index.html"))

# Mount the script directory as a file server at the root
app.mount("/", StaticFiles(directory=script_directory), name="root")

# Entry point to launch the server directly
if __name__ == "__main__":
    port = 8080  # Define the port number
    url = f"http://127.0.0.1:{port}/home"

    # Fancy console output
    console.print("[bold magenta]##############################################[/bold magenta]")
    console.print("[bold magenta]#[/bold magenta] [bold cyan]NewGen FashionDesigner powered by GenAI[/bold cyan] [bold magenta]#[/bold magenta]")
    console.print("[bold magenta]##############################################[/bold magenta]\n")
    
    console.print("[bold magenta]Starting the FastAPI server...[/bold magenta]")
    for i in range(3):
        console.print(f"[cyan]Launching in {3 - i}...[/cyan]")
        time.sleep(1)

    console.print(f"[bold green]Server is live![/bold green] :rocket:")
    console.print(f"[bold yellow]Link:[/bold yellow] [underline blue]{url}[/underline blue]")

    # Launch the server
    uvicorn.run(app, host="127.0.0.1", port=port, reload=False)
