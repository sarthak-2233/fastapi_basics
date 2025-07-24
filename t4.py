from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class User(BaseModel):
    name:str
    age:int
"""
@app.post('/users/')
def create_user(user:User):
    return {"sender user name":user.name,"sender age":user.age}
"""

@app.get('/users/{user_id}',response_model=User)
def show_data(user_id:int):
    return{"name":'s',"age":23}