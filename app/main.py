from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Sentiment Analyzer API")
app.include_router(router)
