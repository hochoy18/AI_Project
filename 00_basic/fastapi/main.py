from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/items")
def get_items():
    return ["apple", "banana"]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.post("/login")
def login(username: str, password: str):
    return {"username": username,
            "password": password,
            "message": "Welcome {}, you log success".format(username),
            }