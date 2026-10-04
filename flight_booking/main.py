from fastapi import FastAPI
from models.book_flight import BookingInformation


app = FastAPI()

@app.post("/booking")
async def book_flight(information: BookingInformation):
    return information