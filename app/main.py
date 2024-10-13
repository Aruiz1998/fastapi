from fastapi import FastAPI
from passlib.context import CryptContext

from . import models
from .database import engine
from .routers import posts, user, auth, vote

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated='auto')

app = FastAPI()

app.include_router(posts.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message" : "Hello World"}

