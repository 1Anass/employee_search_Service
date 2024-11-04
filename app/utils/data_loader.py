import pandas as pd

def load_employee_data(file_path):
    """
    Loads the employee data from the specified CSV file.
    
    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing employee data.
    """
    return pd.read_csv(file_path)

def load_all_data(uk_file_path, us_file_path):
    """
    Loads and combines UK and US employee data from CSV files.
    
    Args:
        uk_file_path (str): Path to the UK employee CSV file.
        us_file_path (str): Path to the US employee CSV file.
    
    Returns:
        dict: Dictionary with two DataFrames, for UK and US employees.
    """
    uk_data = load_employee_data(uk_file_path)
    us_data = load_employee_data(us_file_path)
    
    return {'UK': uk_data, 'US': us_data}
