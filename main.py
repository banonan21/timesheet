from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, admin, timesheet

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Timesheet API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])
app.include_router(timesheet.router, prefix="/timesheet", tags=["Timesheet"])

@app.get("/")
def root():
    return {"message": "Timesheet API running"}
