from fastapi import FastAPI
from routers import blogs,users,authentication
import models,database



models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()
app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)



@app.get('/')
def root():
    return {'welcome':'welcome to api'}









    


    

