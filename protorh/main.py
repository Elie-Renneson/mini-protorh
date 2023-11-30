from model.employee import Employee, EmployeeCreate
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os

app = FastAPI()
DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to allow specific origins
    allow_methods=["*"],  # Adjust this to allow specific methods (e.g., ["GET", "POST"])
    allow_headers=["*"],  # Adjust this to allow specific headers
)


@app.get("/")
async def hello():
    return {"message": "Hello World!!!"}


# Endpoint to create an employee
@app.post("/employees/", response_model=Employee)
def create_employee(employee: EmployeeCreate):
    db = SessionLocal()
    try:
        # Insert the new employee into the database
        query = text("INSERT INTO employee (first_name, last_name, email, department, hire_date) "
                     "VALUES (:first_name, :last_name, :email, :department, :hire_date) "
                     "RETURNING employeeID")
        params = employee.dict()
        result = db.execute(query, params)
        employee_id = result.scalar()
        db.commit()
        db.close()
        return {"employeeID": employee_id, **employee.dict()}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))