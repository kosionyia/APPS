from pydantic import BaseModel, EmailStr, Field, field_validator
import re 


class UserRegsitration(BaseModel):
    username: str = Field(min_length=3, max_length=8)
    email: EmailStr 
    password: str = Field(min_length=8, )

    @field_validator("password")
    @classmethod
    def validate_password(cls, password: str):
        if len(password) <8:
            raise ValueError("Password must be at least 8characcters long")

        if not re.search(r"[A-Z]", password):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", password):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"[0-9]",password):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[^a-zA-Z0-9]", password):
            raise ValueError("Password must contain at least one special character")

        return password

