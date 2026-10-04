from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types import phone_numbers
from datetime import date



class ContactDetails(BaseModel):
    email: EmailStr
    phone_number: phone_numbers

class FlightDetails(BaseModel):
    origin: str
    destination: str
    date: date


class BookingInformation(BaseModel):
    name: str = Field(min_length=3, max_length=120, description="Contact name")
    age: int = Field(gt=5, lt=100, description="Passengers age")
    seat_no: str
    contact_details: ContactDetails
    flight_detials: FlightDetails
