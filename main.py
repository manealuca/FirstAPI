from datetime import date, datetime
from uuid import UUID
from typing import Optional

import pydantic

#Pydantic
from pydantic import BaseModel, EmailStr,Field

#FasApi
from fastapi import FastAPI


class UserBase(BaseModel):
    user_id: UUID= Field(...)
    email:EmailStr = Field(...)




class UserLogin(UserBase):
    password: str = Field(...,min_length=8,max_length=40)    




class User(UserBase):
    first_name: str = Field(...,min_length=1,max_length=50,example="Luca")
    last_name: str = Field(...,min_length=1,max_length=50,example="Manea")
    birth_date:Optional[date] = Field(default=None)




class Tweet(BaseModel):
    tweet_id: UUID = Field(...)
    content: str = Field(...,min_length=1,max_length=255)
    created_at: datetime = Field(default=datetime.now())
    update_at:Optional[datetime] = Field(default=datetime.now())
    by:User = Field(...)




app = FastAPI()
@app.get(path="/")
def home():
    return {"Twitter API": "Working!"}

if __name__=="__main__":
    import uvicorn
    #uvicorn.run(app,host="localhost",port=8000,)
    uvicorn.run('main:app',host="127.0.0.1",port=8000,reload=True)
    