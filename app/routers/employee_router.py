from fastapi import APIRouter, Depends
from typing import List
from app.services.employee_service import get_all_by_name
from app.dependencies import get_employee_data
from app.models.employee import Employee

router = APIRouter()

@router.get("/employees", response_model=List[Employee])
async def get_all_employees_by_name(name: str, data=Depends(get_employee_data)):
    """
    Endpoint to get all employees matching the provided name.
    
    Args:
        name (str): The name to search for.
        data (dict): The loaded employee data from main.
    
    Returns:
        List[Employee]: List of employees that match the search criteria.
    """
    results = get_all_by_name(name, data)
    return results
