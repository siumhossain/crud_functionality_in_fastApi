from fastapi import APIRouter,Depends,Response,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
from hashing import Hash
from crud import user

get_db = database.get_db

router = APIRouter(
    tags=["Users"],
    prefix = "/user"
)
@router.post('/',response_model=schemas.UserShow)
def createUser(request:schemas.User,db: Session=Depends(get_db)):
    return user.create(request,db)
@router.get('/allUser/',response_model=List[schemas.UserShow])
def get_all_user(db: Session=Depends(get_db)):
    return user.show(db)

@router.post('/{id}',response_model=schemas.UserShow)
def get_singleUser(id,db: Session=Depends(get_db)):
    return user.showById(id,db)