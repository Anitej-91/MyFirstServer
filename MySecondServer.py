from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

file_path = r"./data.json"
with open(file_path,'r') as file:
    userdata = json.load(file)

class USER(BaseModel):
    name: str
    age: int
    married: bool

@app.get('/')
async def home_page():
    return {"Response":"Welcome to the Home Page!"}

@app.get('/get-user-data/{user_id}')
async def send_user_data(user_id: int):
    key = str(user_id)
    if key in userdata:
        return userdata[key]
    else:
        return {"Response": "User not found!"}

@app.post('/send-user-data/{user_id}')
async def take_user_data(user_id: int, User: USER):
    key = str(user_id)
    if key in userdata:
        return {"Response": "User data already exists!"}
    userdata[key] = User.dict()
    with open(file_path, 'w') as File:
        json.dump(userdata, File, indent=3)
    return {"Response": "User data successfully added!"}
