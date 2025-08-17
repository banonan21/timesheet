from pydantic import BaseModel

class EmployeeBase(BaseModel):
    username: str
    fullname: str
    department: str
    position: str

class EmployeeCreate(EmployeeBase):
    pin: str

class EmployeeOut(EmployeeBase):
    id: int
    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    username: str
    pin: str

class ChangePinRequest(BaseModel):
    username: str
    old_pin: str
    new_pin: str

class TimesheetCreate(BaseModel):
    project_no: str
    task: str
    hours: int

class TimesheetOut(TimesheetCreate):
    id: int
    class Config:
        orm_mode = True
