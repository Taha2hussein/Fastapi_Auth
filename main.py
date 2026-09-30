from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from database import engine, Base
from routers import blog, user, authentication

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"data": "Hello Customer welcome to our restaurant app"}


@app.get("/about")
def about():
    return {"data": {"message": "This is a restaurant app"}}


@app.get("/all_resturant")
def getAllResturant():
    return {"data": {"resturant1": "KFC", "resturant2": "McDonalds", "resturant3": "Dominos"}}


@app.get("/specific_resturant")
def getSpecificResturant(resturant_id: int, published: bool, limit: int):
    if published:
        return {"data": {"resturant_id": resturant_id, "published": published, "limit": limit}}


class Resturantsss(BaseModel):
    title: str
    describtion: str
    location: Optional[str] = None


@app.post("/create_resturant")
def create_resturant(request: Resturantsss):
    return request
