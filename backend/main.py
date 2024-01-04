from fastapi import Depends, FastAPI, HTTPException, logger, status
from sqlalchemy.orm import Session
from . import crud   
from . import models
from . import schemas
from backend.database import engine, SessionLocal
from backend.crud import create_employee, get_employee, update_employee, delete_employee
from backend.schemas import EmployeeCreate, Employee



models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency to get the database session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user



# Employee functions
# .......................

# Create employee
@app.post("/employees/", response_model=Employee)
def create_employee_route(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)



@app.get("/employees/", response_model=list[schemas.Employee])
def read_employees(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    employees = crud.get_employees(db, skip=skip, limit=limit)
    return employees



# Get a specific employee
@app.get("/employees/{employee_id}", response_model=Employee)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee(db, employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

# Update employee
@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee_route(employee_id: int, employee: EmployeeCreate, db: Session = Depends(get_db)):
    updated_employee = update_employee(db, employee_id, employee)
    if updated_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

# Delete employee
@app.delete("/employees/{employee_id}", response_model=Employee)
def delete_employee_route(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = delete_employee(db, employee_id)
    if deleted_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return deleted_employee

