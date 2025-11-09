from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_api_key
from db_functions import add_api

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str

class API(BaseModel):
    api_id: int
    key: str
    user_id: int

@app.get("/health")
def health():
    return {"Healthy!!"}

@app.post("/user")
def create_user(user: User):
    return {"user id": user.user_id}

@app.get("/api/{user_id}")
def create_api_for_user(user_id: int):
    key = generate_api_key()
    add_api(api_key=key, user_id=user_id)
    return {"api_key": key}