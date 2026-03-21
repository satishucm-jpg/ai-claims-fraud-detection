from fastapi import FastAPI
from app.api.routes import router
from app.db.database import engine
from app.db.models import Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(router)