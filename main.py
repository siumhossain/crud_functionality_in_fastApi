from fastapi import FastAPI,Depends,Response,status,HTTPException
import schemas,models,database
from sqlalchemy.orm import Session
from database import SessionLocal
from fastapi.encoders import jsonable_encoder
from typing import List
from hashing import Hash



models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def root():
    return {'welcome':'welcome to api'}

@app.post('/blog/')
def create_post(request:schemas.Blog,db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog/',response_model=List[schemas.ShowBlog])
def get_blog(db: Session=Depends(get_db)):
    return db.query(models.Blog).all()
@app.get('/blog/{id}/',status_code=200)
def get_blog_id(id,db: Session=Depends(get_db)):
    singleBlog = db.query(models.Blog).filter(models.Blog.id == id).first()
    #print(singleBlog.id)
    if not singleBlog:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'error':f'blog with this id number {id} not belongs in database'}
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"blog with this {id} id not found")
    return singleBlog
@app.delete('/blog/{id}')
def delete_post(id,db: Session=Depends(get_db)):
    delete_blog = db.query(models.Blog).filter(models.Blog.id==id)
    #print(delete_blog)
    if not delete_blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'this id:-{id} is not avaiable in our data base')
    delete_blog.delete(synchronize_session=False)
    db.commit()
    raise HTTPException(status_code=status.HTTP_202_ACCEPTED,detail='your operation has been successed')
@app.put('/blog/update/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_post(id,request:schemas.Blog,db: Session=Depends(get_db)):
    get_blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not get_blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'this id:-{id} is not avaiable in our data base')
    else:
        update_blog = get_blog.update(dict(request))
        db.commit()
        return request

@app.post('/user/',response_model=schemas.UserShow)
def createUser(request:schemas.User,db: Session=Depends(get_db)):
    user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return request

    


    

