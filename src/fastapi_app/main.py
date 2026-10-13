from fastapi import FastAPI
from fastapi_app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)

# http://localhost:8000/
@app.get("/")
def get_hello():
    return {"Hello": settings.app_name}

# http://localhost:8000/health
@app.get("/health")
def get_health():
    return {"status": "online", "debug": settings.debug}