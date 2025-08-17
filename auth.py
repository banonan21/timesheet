from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(req: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.Employee).filter(models.Employee.username == req.username).first()
    if not user or not bcrypt.verify(req.pin, user.pin):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "employee_id": user.id, "fullname": user.fullname}

@router.post("/change-pin")
def change_pin(req: schemas.ChangePinRequest, db: Session = Depends(get_db)):
    user = db.query(models.Employee).filter(models.Employee.username == req.username).first()
    if not user or not bcrypt.verify(req.old_pin, user.pin):
        raise HTTPException(status_code=401, detail="Invalid old PIN")
    user.pin = bcrypt.hash(req.new_pin)
    db.commit()
    return {"message": "PIN updated successfully"}
