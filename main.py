from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, sessionmaker
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)






@app.get("/")
def index():
    return {"message": "Hello, World!"}





# SCHEMA 
class PostBook(BaseModel):
    id : int 
    title : str
    author : str
    price : int
    quantity : int

    class cofig:
        orm_mode = True



def get_db():
    db = sessionmaker()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]




#REGISTRATION








@app.post("/books", status_code = status.HTTP_201_CREATED)
async def create_book(user:PostBook, db:db_dependency):
    db_books = models.Book(**user.dict())
    db.add(db_books)
    db.commit()


    print(user)                  
    print(f"Creating book: {user.dict()}")  


@app.get("/data")
async def get_alldata(db:db_dependency):
    data = db.query(models.Book).all()
    print()
    if data:
        return data
    else:
        return "Erro no daat"

    


@app.get("/data/{user_id}")
async def get_data(user_id: int, db:db_dependency):
    data = db.query(models.Book).filter(models.Book.id == user_id).first()
    if data:
        return data
    else:
        return "Erro no daat"