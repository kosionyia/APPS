from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class PaymentDetails(BaseModel):
    amount: float = Field( gt=0)
    card_number: str = Field (min_length=15, max_length=15)
    expiration_date: str = Field(
        pattern=r"^(0[1-9]|1[0-2])\/([0-9]{2})$"
    )
    cvv: int = Field(min_length=3)

    @field_validator("card_number", "cvv")
    @classmethod
    def numeric_fields(cls, num: str) -> str:
        if not num.isdigit():
            raise ValueError("Must contain only numbers")
        return num

    @field_validator("expiration_date")
    @classmethod
    def validate_expiration_date(cls, date: str) -> str:
        month, year = date.split("/")
        expiration = datetime.strptime(f"{month}/{year}", "%m/%y")

        current = datetime.now()

        if expiration.year < current.year or (
            expiration.year == current.year and expiration.month < current.month
        ):
            raise ValueError("Card has expired")

        return date