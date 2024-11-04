from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    company: str
    address: str
    city: str
    phone: str
    email: str
    salary: float