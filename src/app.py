from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(title="Log Analyzer")
app.include_router(router)
