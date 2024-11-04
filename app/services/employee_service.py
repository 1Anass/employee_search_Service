from app.models.employee import Employee

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
    
    for country, df in data.items():
        # Search by first or last name for single-word input
        filtered = df[(df['first_name'].str.lower() == name) | (df['last_name'].str.lower() == name)]
        
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
