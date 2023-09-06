from http.client import HTTPMessage
from typing import List
from fastapi import FastAPI, Depends, HTTPException
from models import LearnerModel
from database import engine, SessionLocal
import models
from sqlalchemy.orm import Session
from prometheus_client import start_http_server, Counter

METRICS_PORT = 8001
REQUEST_COUNT = Counter('app_request_count', 'Total / http request count')
REQUEST_COUNT_LEARNERS = Counter('app_request_count_users', 'Total /api/v1/learners http request count')

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

start_http_server(METRICS_PORT)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def create_database():
    REQUEST_COUNT.inc()
    return {"Hello": "Learners!"}

@app.get("/api/v1/learners")
async def fetch_users(db: Session = Depends(get_db)):
    REQUEST_COUNT_LEARNERS.inc()
    return db.query(models.Learner).all()

@app.post("/api/v1/learners")
async def register_user(learner: LearnerModel, db: Session = Depends(get_db)):
    learner_model = models.Learner()
    learner_model.id_learner = learner.id_learner
    learner_model.first_name = learner.first_name
    learner_model.last_name = learner.last_name
    db.add(learner_model)
    db.commit()
    return {"id": learner.id_learner}

@app.delete("/api/v1/learners/{id_learner}")
async def delete_user(id_learner: int, db: Session = Depends(get_db)):
    learner_model = db.query(models.Learner).filter(models.Learner.id_learner == id_learner).first()

    if learner_model is not None:
        db.delete(learner_model)
        db.commit()
        return {f"user with id: {id_learner} was deleted"}

    else:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {id_learner} does not exist"
        )

@app.put("/api/v1/learners/{learner_id}")
async def update_user(learner_id: int, learner: LearnerModel, db: Session = Depends(get_db)):
    learner_model = db.query(models.Learner).filter(models.Learner.id_learner == learner_id).first()
    if not learner_model:
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {learner_id} does not exist"
        )
    
    learner_model.first_name = learner.first_name
    learner_model.last_name = learner.last_name
    db.commit()
    return {"message": f"user with id: {learner_id} was updated"}


