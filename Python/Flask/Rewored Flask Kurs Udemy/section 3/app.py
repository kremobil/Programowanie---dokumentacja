from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Item 1",
                "price": 10
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"stores": stores}

@app.post("/store/<string:store_name>")
def create_store(store_name:str) -> dict:
    store = {
        "name": store_name,
        "items": []
    }
    stores.append(store)
    return store

@app.post("/store/<string:store_name>/<string:item>")
def create_item(store_name:str, item:str) -> dict:
    for store in stores:
        print(store, store_name)
        if store["name"] == store_name:
            store["items"].append({
                "name": item,
                "price": request.json["price"]
            })
            return store
    return {"error": "Store not found"}

@app.get("/store/<string:store_name>")
def get_store(store_name:str) -> dict:
    for store in stores:
        if store["name"] == store_name:
            return store
    return {"error": "Store not found"}

@app.get("/store/<string:store_name>/items")
def get_store_items(store_name:str) -> dict:
    for store in stores:
        if store["name"] == store_name:
            return { "items": store["items"] }
    return {"error": "Store not found"}

