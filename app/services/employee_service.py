from app.models.employee import Employee
from io import BytesIO
from typing import Optional
import matplotlib.pyplot as plt
from fastapi.responses import StreamingResponse

def get_all_by_name(name, data):
    """
    Searches for all employees by name (first or last name) in the provided data.
    
    Args:
        name (str): The name to search for.
        data (dict): Loaded employee data (UK and US).
    
    Returns:
        List[Employee]: List of employees matching the search criteria.
    """
    results = []
    name = name.lower()
    name_parts = name.split()

    for country, df in data.items():
        if len(name_parts) == 1:
            # Single-word input: match either first_name or last_name
            filtered = df[(df['first_name'].str.lower() == name) | (df['last_name'].str.lower() == name)]
        else:
            # Multiple-word input: match last word with last_name, and the rest with first_name
            first_name_part = " ".join(name_parts[:-1])
            last_name_part = name_parts[-1]
            filtered = df[
                (df['first_name'].str.lower() == first_name_part) & 
                (df['last_name'].str.lower() == last_name_part)
            ]

        for _, row in filtered.iterrows():
            # Construct country-specific address and phone
            address = (f"{row['address']}, {row['city']}, "
                       f"{row['county'].upper()}, {row['postal']}, UK" if country == 'UK' 
                       else f"{row['address']}, {row['city']}, {row['state']}, {row['zip']}, USA")
            phone = f"+44 {row['phone']}" if country == 'UK' else f"+1 {row['phone']}"
            
            # Append formatted employee record to results
            results.append(Employee(
                name=f"{row['first_name']} {row['last_name']}",
                company=row['company_name'],
                address=address,
                city=row['city'],
                phone=phone,
                email=row['email'],
                salary=row['salary']
            ))
    
    return results

def get_wage_distribution(company_name: str, data: dict, country: Optional[str] = None) -> BytesIO:
    """
    Generates a wage distribution plot for the specified company and returns it as a PNG image.
    
    Args:
        company_name (str): The name of the company.
        data (dict): Dictionary containing employee data for UK and US.
        country (Optional[str]): Country filter ('UK' or 'US'). If None, use data from both countries.
    
    Returns:
        BytesIO: A BytesIO object containing the PNG image of the wage distribution.
    """
    # Validate country parameter
    if country and country not in ["UK", "US"]:
        raise ValueError("Country must be 'UK' or 'US'.")

    # Filter data by company name and country
    salaries = []
    if country:
        # Use only the data from the specified country
        if country in data:
            df = data[country]
            filtered_df = df[df['company_name'].str.lower() == company_name.lower()]
            salaries = filtered_df['salary'].tolist()
    else:
        # Use data from both UK and US
        for country_df in data.values():
            filtered_df = country_df[country_df['company_name'].str.lower() == company_name.lower()]
            salaries.extend(filtered_df['salary'].tolist())
    
    if not salaries:
        raise ValueError("No salary data found for the specified company and country.")

    # Create the histogram plot
    plt.figure(figsize=(10, 6))
    plt.hist(salaries, bins=10, color='skyblue', edgecolor='black')
    plt.title(f'Wage Distribution for {company_name}')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')

    # Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    return buf
