from fastapi import APIRouter,Depends,Response,status,HTTPException
from typing import List
import schemas,database,models
from sqlalchemy.orm import Session
from crud import blog,user

get_db = database.get_db
router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)
@router.get('/',response_model=List[schemas.ShowBlog])
def get_blog(db: Session=Depends(get_db)):
    return blog.get(db)

@router.get('/{id}/',status_code=200,response_model=schemas.ShowBlog,tags = ['Blogs'])
def get_blog_id(id,db: Session=Depends(get_db)):
    return blog.one_blog(id,db)
    

@router.post('/')
def create_post(request:schemas.ShowBlog,db: Session=Depends(get_db)):
    return blog.create(request,db)
    
@router.put('/update/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Blogs"])
def update_post(id,request:schemas.Blog,db: Session=Depends(get_db)):
    return blog.update(id,request,db)

@router.delete('/{id}',tags = ["Blogs"])
def delete_post(id,db: Session=Depends(get_db)):
    return blog.delete(id,db)
