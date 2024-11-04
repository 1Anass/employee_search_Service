# app/main.py

from fastapi import FastAPI, Depends
from app.utils.data_loader import load_all_data
from app.routers import employee_router
from app.config import UK_DATA_PATH, US_DATA_PATH

app = FastAPI()

# Global variable to store data
employee_data = {}

@app.on_event("startup")
async def startup_event():
    """
    Load employee data from CSV files on app startup.
    """
    global employee_data
    employee_data = load_all_data(UK_DATA_PATH, US_DATA_PATH)

def get_employee_data():
    """
    Dependency to access the loaded employee data.
    """
    return employee_data

# Include employee router
app.include_router(employee_router.router, prefix="/api")
