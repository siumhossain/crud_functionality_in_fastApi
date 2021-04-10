from sqlalchemy.orm import Session
import schemas,database,models
from fastapi import APIRouter,Depends,Response,status,HTTPException

def get(db:Session):
    return db.query(models.Blog).all()
def one_blog(id,db):
    singleBlog = db.query(models.Blog).filter(models.Blog.id == id).first()
    #print(singleBlog.id)
    if not singleBlog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'error':f'blog with this id number {id} not belongs in database'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"blog with this {id} id not found")
    return singleBlog
def create(request:schemas.ShowBlog,db):
    new_blog = models.Blog(title=request.title,body=request.body,userId=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def update(id,request:schemas.ShowBlog,db):
    get_blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not get_blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'this id:-{id} is not avaiable in our data base')
    else:
        update_blog = get_blog.update(dict(request))
        db.commit()
        return request
def delete(id,request:schemas.ShowBlog,db):
    delete_blog = db.query(models.Blog).filter(models.Blog.id==id)
    #print(delete_blog)
    if not delete_blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'this id:-{id} is not avaiable in our data base')
    delete_blog.delete(synchronize_session=False)
    db.commit()
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail='your operation has been successed')