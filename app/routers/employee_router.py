from fastapi import APIRouter, Depends, HTTPException, Query
from typing import List
from app.services.employee_service import get_all_by_name, get_wage_distribution
from app.dependencies import get_employee_data
from app.models.employee import Employee
from typing import Optional
from fastapi.responses import StreamingResponse

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

@router.get("/wage_stats")
async def get_wage_stats(
    company_name: str,
    country: Optional[str] = Query(None, regex="^(UK|US)$"),  # Validate country as 'UK' or 'US' only
    data=Depends(get_employee_data)
):
    """
    Endpoint to get the wage distribution plot for a specific company.
    
    Args:
        company_name (str): The name of the company.
        country (str, optional): Country filter ('UK' or 'US').

    Returns:
        StreamingResponse: Image of the wage distribution.
    """
    try:
        # Call the wage distribution function
        img = get_wage_distribution(company_name, data, country)
        # Return the image as a streaming response with 'image/png' media type
        return StreamingResponse(img, media_type="image/png")
    except ValueError as e:
        # Handle cases where the company or country data is not found
        raise HTTPException(status_code=404, detail=str(e))