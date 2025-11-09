from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    user_id: int
    name: str

@app.get("/health")
def health():
    return {"Healthy!!"}

@app.post("/user")
def create_user(user: User):
    return {"user id": user.user_id}