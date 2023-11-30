from pydantic import BaseModel

# Define Pydantic models to represent the data
class EmployeeCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    department: str
    hire_date: str

class Employee(BaseModel):
    employeeID: int
    first_name: str
    last_name: str
    email: str
    department: str
    hire_date: str
