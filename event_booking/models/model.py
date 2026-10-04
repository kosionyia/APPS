from datetime import date
from pydantic import BaseModel, Field



class EventBooking(BaseModel):
    attendee_name: str = Field(
        min_length=2,
        max_length=50
    )

    email: str = Field(
        min_length=5,
        max_length=100
    )

    age: int = Field(
        ge=18,
        le=100
    )

    event_name: str = Field(
        min_length=2,
        max_length=100
    )

    event_date: date

    location: str = Field(
        min_length=2,
        max_length=100
    )

    ticket_type: str


