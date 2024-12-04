# app/main.py
from fastapi import FastAPI
from app.api.routes import auth, emails,health_check, users # Import the routers

app = FastAPI()

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(emails.router, prefix="/email", tags=["email"])
app.include_router(health_check.router, prefix="/health", tags=["health"]) 
app.include_router(users.router, prefix="/users", tags=["users"]) 
