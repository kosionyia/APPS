from fastapi import FastAPI
from models.payment import PaymentDetails



app = FastAPI()

@app.post("/payments")
async def process_payment(payment: PaymentDetails):

    if payment.cvv == "000":
        return {
            "status": "failed",
            "message": "Payment authentication failed"
        }

    return {
        "status": "success",
        "message": "Payment processed successfully",
        "amount": payment.amount
    }
