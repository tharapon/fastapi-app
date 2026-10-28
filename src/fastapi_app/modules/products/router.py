from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/products", tags=["Products"])

products = [
    {"id": 1, "name": "Mouse", "price": 590, "stock": 10},
    {"id": 2, "name": "Keyboard", "price": 1290, "stock": 5},
    {"id": 3, "name": "Monitor", "price": 4990, "stock": 2},
]

# http://localhost:8000/api/v1/products
# GET  `/api/v1/products`  
# คืนสินค้าทั้งหมด 
@router.get("/")
def get_products():
    return products

# http://localhost:8000/api/v1/products/{product_id}
# GET `/api/v1/products/{product_id}`
# คืนสินค้าตาม id 
@router.get("/{product_id}")
def get_product_by_id(product_id: int):
    product = next((item for item in products if item["id"] == product_id), None)

    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    
    return product

# http://localhost:8000/api/v1/products
# POST `/api/v1/products`      
# เพิ่มสินค้า ตอบกลับด้วยคำว่า success และ status_code=201
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(name: str, price: int, stock: int):
    new_product = {
        "id": (max((item["id"] for item in products), default=0)) + 1 ,
        "name": name, "price": price, 
        "stock": stock}
    products.append(new_product)
    return {"status": "success", "product": new_product}
