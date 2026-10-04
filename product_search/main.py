from fastapi import FastAPI, Query



app = FastAPI()

products = [
    {
        "product_name": "iPhone 15",
        "category": "electronics",
        "price": 150000
    },
    {
        "product_name": "Samsung Galaxy S24",
        "category": "electronics",
        "price": 180000
    },
    {
        "product_name": "Nike Air Max",
        "category": "shoes",
        "price": 85000
    },
]


@app.get("/search")
async def search_product(
    product_name: str = Query(min_length=4, description="What is your Product name?"),
    category: str = Query(min_length=5, description="Product category"),
    min_price: int = Query(ge=0, description="Minimum price range"),
    max_price: int = Query(ge=0, description="Maximum price range")
):

    results = []

    for product in products:
        if (
            product_name.lower() in product["product_name"].lower() and
            category.lower() == product["category"].lower() and 
            min_price <= product["price"] <= max_price
        ):
            results.append(product)
            
    return results
