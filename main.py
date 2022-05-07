from datetime import date, datetime
import json
from turtle import st
from unittest import result
from uuid import UUID
from typing import Optional, List

import pydantic

#Pydantic
from pydantic import BaseModel, EmailStr,Field

#FasApi
from fastapi import Body, FastAPI, status


class UserBase(BaseModel):
    user_id: UUID= Field(...)
    email:EmailStr = Field(...)




class UserLogin(UserBase):
    password: str = Field(...,min_length=8,max_length=40)    




class User(UserBase):
    first_name: str = Field(...,min_length=1,max_length=50,example="Luca")
    last_name: str = Field(...,min_length=1,max_length=50,example="Manea")
    birth_date:Optional[date] = Field(default=None)



class UserRegister(User,UserLogin):
    pass




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
def signup(user:UserRegister = Body(...)):
    """
    Title: SignUp
    This path operation register a user in the app

    Parameters:
        -Request Body Parameter
            -user: UserRegister
            
    Returns a JSON with the basic user information:
        -user_id: UUID
        -email: Emailstr
        -first_name: str
        -last_name:str
        -birth_date: date
    """
    with open('users.json','r+',encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] =str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        
    #with open('filepath','r+') as f: result = json.load(f)
    #modifica el archivo
    #json.dump(result,f)
        return user
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
    """This path operation show all users in the app
    Parameters:
        user_id: UUID
        email: Emailstr
        first_name: str
        last_name: str
        birth_date: date
    """
    with open("users.json","r",encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

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
    