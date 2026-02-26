from fastapi import FastAPI
from app.routes.internship_routes import router as internship_router

app = FastAPI()

app.include_router(internship_router)