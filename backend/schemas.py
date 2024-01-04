
from pydantic import BaseModel
from typing import List
from datetime import date

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str



class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str = None
    date_of_birth: date = None
    position: str
    department: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        orm_mode = True
