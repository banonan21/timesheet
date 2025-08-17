from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    pin = Column(String)  # hashed PIN
    fullname = Column(String)
    department = Column(String)
    position = Column(String)

    timesheets = relationship("Timesheet", back_populates="employee")

class Timesheet(Base):
    __tablename__ = "timesheets"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    project_no = Column(String)
    task = Column(String)
    hours = Column(Integer)

    employee = relationship("Employee", back_populates="timesheets")
