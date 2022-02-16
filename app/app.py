from fastapi import FastAPI , Depends
from . import schemas ,models
from . database import engine, SessionLocal
from pydantic import BaseModel
from sqlalchemy.orm import Session

app=FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
	db=SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.get('/', tags=['ROOT'])
def root()->dict:
	return {
	"Hello" : "World"
	}


#create
@app.post('/todo')
def create(request:schemas.DO , db: Session=Depends(get_db)):
	new_todo=models.DO(id=request.id,task=request.task, assigned_to=request.assigned_to,is_completed=request.is_completed,due_date=request.due_date)
	db.add(new_todo)
	db.commit()
	db.refresh(new_todo)
	return new_todo

#read
@app.get('/todo')
def activity(db: Session=Depends(get_db)):
	activity_all=db.query(models.DO).all()
	return activity_all

#delete
@app.delete('/todo/{id}')
def clear(id, db: Session=Depends(get_db)):
	db.query(models.DO).filter(models.DO.id==id).delete(synchronize_session=False)
	db.commit()
	return "deleted "

#update
@app.put('/todo/{id}')
def updates(id, request:schemas.DO, db: Session=Depends(get_db)):
	db.query(models.DO).filter(models.DO.id==id).update({"task": request.task})
	db.query(models.DO).filter(models.DO.id==id).update({"is_completed": request.is_completed})
	db.commit()
	return "updated"
	#return request
