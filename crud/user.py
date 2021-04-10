from fastapi import Depends,Response,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
from hashing import Hash


def create(request:schemas.User,db):
    user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return request
def show(db):
    return db.query(models.User).all()

def showById(id,db):
    get_user = db.query(models.User).filter(models.User.id == id).first()
    if not get_user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'this id:-{id} is not avaiable in our data base')
    return get_user