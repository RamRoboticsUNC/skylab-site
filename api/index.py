from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

# Create FastAPI app
app = FastAPI(title="Carolina Skylab", description="Carolina Skylab Site")

# Get the directory where this file is located
BASE_DIR = Path(__file__).parent.parent

# Setup templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Serve favicon
@app.get("/favicon.ico")
def favicon():
    """Serve favicon from root"""
    return FileResponse(
        str(BASE_DIR / "static" / "favicon.ico"),
        media_type="image/x-icon"
    )

# Mount static files
app.mount("/assets", StaticFiles(directory=str(BASE_DIR / "static" / "assets")), name="assets")
app.mount("/images", StaticFiles(directory=str(BASE_DIR / "static" / "images")), name="images")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """Serve the main page"""
    return templates.TemplateResponse("index.html", {"request": request})

# For local development with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
