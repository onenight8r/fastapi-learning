from fastapi import FastAPI, HTTPException, status
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app=FastAPI()

class Post(BaseModel):
    title:str
    content:str
# Pydantic is a data validation and parsing library in Python.
# It's often used with frameworks like FastAPI for data validation in APIs.
# Pydantic allows you to define data models using Python classes, and it validates
# the data automatically when creating instances of those classes.



@app.get("/login")
def root():

    return {"message": "they ius the updated one in the  World"}

@app.get("/posts")#In FastAPI, the @ symbol is used for decorators,
#which are a way to modify or extend the behavior of functions or classes.
def get_post():
    return{"x":my_posts}

#f you have multiple functions after a decorator, only the first function will be affected by the decorator.

my_posts=[{"title":"title of the post 1","content":"content of post 1","id":1},
           {"title":"fav fodd items","content":"i like pizza and pasta","id":2}]


@app.post("/posts")
def create_posts(new_post: Post):
    post_dict=new_post.dict()#In Pydantic (a data validation library often used with FastAPI), a model instance can be converted to a dictionary using the dict() method.
    post_dict['id']=randrange(0,100000000)
    my_posts.append(post_dict)
    print(my_posts)
    return{"data":new_post}


def find_posts(id):
    for p in my_posts:
        if p["id"]==id:
            return p




@app.get("/posts/{id}") #id is the path parameter
def get_post(id:int):#fast API can convert it to the integer
    print(id)
    post=find_posts(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found") # to change the error code to a specifc effor code under certain codnition
    return{"result":post}

@app.get("/posts/latest")
def get_latest_posted():
    return get_post[len(get_post)-1]
#the route is woks as top down, latest url shall be matched with the posts/{id} path,
#we can move it up or think of other api

#how order routing works here in fastAPI