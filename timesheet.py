from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submit", response_model=schemas.TimesheetOut)
def submit_timesheet(emp_id: int, entry: schemas.TimesheetCreate, db: Session = Depends(get_db)):
    ts = models.Timesheet(employee_id=emp_id, project_no=entry.project_no, task=entry.task, hours=entry.hours)
    db.add(ts)
    db.commit()
    db.refresh(ts)
    return ts

@router.get("/mytimesheets", response_model=list[schemas.TimesheetOut])
def get_timesheets(emp_id: int, db: Session = Depends(get_db)):
    return db.query(models.Timesheet).filter(models.Timesheet.employee_id == emp_id).all()
