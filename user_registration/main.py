from fastapi.testclient import TestClient
from models.user_reg import UserRegsitration
from fastapi import FastAPI
import bcrypt
    
app = FastAPI()

@app.post("/register")
async def register_user(user: UserRegsitration):

    hashed_pw = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    return {
        "message": "User registered succesfully",
        "email": user.email,
        "password": hashed_pw
    }

client = TestClient(app)

response = client.post(
    "/register",
    json={
        "username": "kosi123",
        "email": "kosi@example.com",
        "password": "Password123!"
    }
)

print(response.status_code)
print(response.json())
