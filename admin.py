from fastapi import APIRouter, Depends
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

@router.post("/add", response_model=schemas.EmployeeOut)
def add_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_emp = models.Employee(
        username=emp.username,
        fullname=emp.fullname,
        department=emp.department,
        position=emp.position,
        pin=bcrypt.hash(emp.pin)  # store hashed PIN
    )
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp

@router.get("/list", response_model=list[schemas.EmployeeOut])
def list_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()
