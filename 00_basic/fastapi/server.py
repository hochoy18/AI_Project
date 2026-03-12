from fastapi import FastAPI
from pydantic import *

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
    """
curl --request POST \
  --url 'http://localhost:8000/login?username=hochoy&password=fd2333' \
  --header 'content-type: application/json'
    :param username:
    :param password:
    :return:
    """
    return {"username": username,
            "password": password,
            "message": "Welcome {}, you log success".format(username),
            }


class User(BaseModel):
    name: str
    age: int
    gender: str


@app.post("/users")
def create_user(user: User):
    """
curl --request POST \
  --url http://localhost:8000/users \
  --header 'content-type: application/json' \
  --data '{
  "name": "zhangsan",
  "age": 11,
  "gender": "F"
}'
    :param user:
    :return:
    """
    return {
        "code": 201,
        "message": "User created",
        "user": user.dict()
    }