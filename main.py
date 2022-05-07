from datetime import date, datetime
from turtle import st
from uuid import UUID
from typing import Optional, List

import pydantic

#Pydantic
from pydantic import BaseModel, EmailStr,Field

#FasApi
from fastapi import FastAPI, status


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
#Users
### create a user
@app.post(path="/signup",response_model=User,
          status_code=status.HTTP_201_CREATED,
          summary="Register a user",
          tags=["Users"])
def signup():
    pass

### login user
@app.post(path="/login",response_model=User,
          status_code=status.HTTP_200_OK,
          summary="Login a user",
          tags=["Users"])
def login():
    pass

### show all  users
@app.get(path="/users",response_model=List[User],
          status_code=status.HTTP_200_OK,
          summary="Show all users",
          tags=["Users"])
def show_all_users():
    pass

###show a user
@app.post(path="/users/{user_id}",response_model=User,
          status_code=status.HTTP_200_OK,
          summary="Show a user",
          tags=["Users"])
def show_user():
    pass

### delete a user
@app.delete(path="/users/{user_id}/delete",response_model=User,
          status_code=status.HTTP_200_OK,
          summary="Delete a user",
          tags=["Users"])
def delete_user():
    pass


###update a user
@app.put(path="/users/{user_id}/update",response_model=User,
          status_code=status.HTTP_200_OK,
          summary="Update a user",
          tags=["Users"])
def update_user():
    pass

###shoe all tweets
#Tweets
@app.get(path="/",response_model=List[Tweet],status_code=status.HTTP_200_OK, summary="Show all tweets",tags=["Tweests"])
def home():
    return {"Twetter API": "Working!"}

###post a tweet
@app.post(path="/",response_model=Tweet,status_code=status.HTTP_201_CREATED, summary="Post a Tweet",tags=["Tweests"])
def post_tweet():
    return{}

###show a tweet
@app.get(path="/tweets/{tweet_id}",response_model=Tweet,status_code=status.HTTP_200_OK, summary="Show a Tweet",tags=["Tweests"])
def show_tweet():
    pass 
###delete a tweet
@app.delete(path="/tweets/{tweet_id}/delete",response_model=Tweet,status_code=status.HTTP_200_OK, summary="Delete a Tweet",tags=["Tweests"])
def delete_tweet():
    pass

###update a tweet
@app.get(path="/tweets/{tweet_id}/update",response_model=Tweet,status_code=status.HTTP_200_OK, summary="Update a Tweet",tags=["Tweests"])
def update_tweet():
    pass


#EntriPoint
###inicial la api
if __name__=="__main__":
    import uvicorn
    #uvicorn.run(app,host="localhost",port=8000,)
    uvicorn.run('main:app',host="127.0.0.1",port=8000,reload=True)
    