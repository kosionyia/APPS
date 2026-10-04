from fastapi import FastAPI, HTTPException
from models.model import EventBooking



app = FastAPI()

AVAILABLE_TICKETS = ["regular", "vip", "premium"]


@app.post("/bookings")
async def book_event(booking: EventBooking):

    if booking.ticket_type.lower() not in AVAILABLE_TICKETS:
        raise HTTPException(
            status_code=400,
            detail="Invalid ticket type. Choose regular, vip, or premium."
        )

    return {
        "message": "Event booking successful",
        "booking": {
            "attendee_name": booking.attendee_name,
            "email": booking.email,
            "age": booking.age,
            "event_name": booking.event_name,
            "event_date": booking.event_date,
            "location": booking.location,
            "ticket_type": booking.ticket_type.lower()
        }
    }