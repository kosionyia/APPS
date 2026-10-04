from fastapi import FastAPI, Query, Path, HTTPException

app = FastAPI()


vehicles = [
    {
        "id": 1,
        "make": "Toyota",
        "model": "Camry",
        "price": 25000000
    },
    {
        "id": 2,
        "make": "Honda",
        "model": "Accord",
        "price": 22000000
    },
    {
        "id": 3,
        "make": "Toyota",
        "model": "Corolla",
        "price": 20000000
    },
    {
        "id": 4,
        "make": "Mercedes",
        "model": "C300",
        "price": 45000000
    }
]


@app.get("/vehicles")
async def get_vehicles(
    make: str | None = Query(
        None,
        min_length=2,
        max_length=30
    ),
    model: str | None = Query(
        None,
        min_length=1,
        max_length=30
    ),
    min_price: float | None = Query(
        None,
        ge=0
    ),
    max_price: float | None = Query(
        None,
        ge=0
    )
):
    filtered_vehicles = vehicles

    if make:
        filtered_vehicles = [
            vehicle
            for vehicle in filtered_vehicles
            if vehicle["make"].lower() == make.lower()
        ]

    if model:
        filtered_vehicles = [
            vehicle
            for vehicle in filtered_vehicles
            if vehicle["model"].lower() == model.lower()
        ]

    if min_price is not None:
        filtered_vehicles = [
            vehicle
            for vehicle in filtered_vehicles
            if vehicle["price"] >= min_price
        ]

    if max_price is not None:
        filtered_vehicles = [
            vehicle
            for vehicle in filtered_vehicles
            if vehicle["price"] <= max_price
        ]

    return filtered_vehicles


@app.get("/vehicles/{vehicle_id}")
async def get_vehicle(
    vehicle_id: int = Path(gt=0)
):
    for vehicle in vehicles:
        if vehicle["id"] == vehicle_id:
            return vehicle

    raise HTTPException(
        status_code=404,
        detail="Vehicle not found"
    )