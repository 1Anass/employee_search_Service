# Employee Search Service

## Overview

The **Employee Search Service** is a RESTful API built using FastAPI that allows users to search for employee data by name and generate wage distribution charts for companies. This service utilizes data from two CSV files (one for UK employees and one for US employees), simulating a database for employee information. Key features include searching employees by name and generating a wage distribution histogram for a specified company, with optional country filtering.

## Key Features

1. **Employee Search by Name**:
   - Allows users to search for employees by a single name (first or last) or full name.
   - Returns employee information including name, company, address (formatted per UK or US standards), phone number, email, and salary.
   
2. **Wage Distribution by Company**:
   - Generates a histogram showing the distribution of salaries for employees of a specified company.
   - Allows optional filtering by country (UK or US).
   - Returns the wage distribution as a PNG image, which can be displayed directly in a browser or downloaded.

## Architecture

### 1. Data Layer
   - Employee data is loaded from two CSV files (`employees_uk.csv` and `employees_us.csv`).
   - Data is read into pandas DataFrames, which are stored in a global dictionary for efficient access.

### 2. Service Layer
   - **`get_all_by_name(name, data)`**: Searches for employees by either first or last name (for single-word queries) or by full name. Returns a list of employee objects that match the query.
   - **`get_wage_distribution(company_name, data, country)`**: Generates a wage distribution histogram for a specific company, optionally filtered by country. Returns the image as a `BytesIO` object.

### 3. API Layer
   - **Endpoints**:
     - **`GET /api/employees?name={name}`**: Searches for employees by name.
     - **`GET /api/wage_stats?company_name={company_name}&country={country}`**: Generates a wage distribution histogram for the specified company.

## API Endpoints

### 1. Employee Search Endpoint
   - **URL**: `/api/employees`
   - **Method**: `GET`
   - **Query Parameter**:
     - `name` (string): The name to search for. Can be either a single name (first or last) or a full name.
   - **Response**:
     - Returns a JSON array of matching employees with the following fields:
       - `name`: Full name of the employee.
       - `company`: Company name.
       - `address`: Formatted address (UK or US format).
       - `city`: City of the employee.
       - `phone`: Formatted phone number with country code.
       - `email`: Email address.
       - `salary`: Employee salary.
   - **Example Request**:
     ```bash
     curl -X GET "http://127.0.0.1:8000/api/employees?name=Evan" -H "accept: application/json"
     ```
   - **Example Response**:
     ```json
     [
         {
             "name": "Evan Zigomalas",
             "company": "Rowley/hansell Petetin",
             "address": "5 Binney St, Abbey Ward, BUCKINGHAMSHIRE, HP11 2AX, UK",
             "city": "Abbey Ward",
             "phone": "+44 01937-864715",
             "email": "evan.zigomalas@gmail.com",
             "salary": 80858
         }
     ]
     ```

### 2. Wage Distribution Endpoint
   - **URL**: `/api/wage_stats`
   - **Method**: `GET`
   - **Query Parameters**:
     - `company_name` (string): The name of the company.
     - `country` (string, optional): The country to filter data by (`"UK"` or `"US"`). If omitted, data from both countries is included.
   - **Response**:
     - Returns a PNG image of the wage distribution histogram.
   - **Example Request**:
     ```bash
     curl -X GET "http://127.0.0.1:8000/api/wage_stats?company_name=Rowley/hansell%20Petetin&country=UK" -H "accept: image/png" --output wage_distribution.png
     ```

## Data Formatting

### Address and Phone Formatting
- **UK**:
  - **Address**: `{address}, {city}, {county (uppercase)}, {postal}, UK`
  - **Phone**: Prefixed with `+44`
- **US**:
  - **Address**: `{address}, {city}, {state}, {zip}, USA`
  - **Phone**: Prefixed with `+1`

## Usage Instructions

1. **Setup**:
   - Clone the repository and navigate to the project directory.
   - Install the dependencies in a virtual environment:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Application**:
   - Start the FastAPI server with `uvicorn`:
     ```bash
     uvicorn app.main:app --reload
     ```
   - The server should be running at `http://127.0.0.1:8000`.

3. **API Documentation**:
   - Access the interactive API documentation provided by FastAPI at `http://127.0.0.1:8000/docs`.

## Testing

- **Unit Tests**:
  - The application includes unit tests for the main service functions.
  - Run the tests with `pytest`:
    ```bash
    pytest
    ```
- **Mock Data**:
  - Tests use mock data to validate the functionality of employee search and wage distribution.

## Assumptions

- **The frontend is responsible for sending well formatted URL params**: For instance, if the company name contains special characters like &, the frontend is responsible for replacing it with %26%.

---

This documentation provides an overview, API usage instructions, and guidance on testing and running the Employee Search Service.
