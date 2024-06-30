import pandas as pd

def load_data(file_path):
    """
    Load the Brent oil prices data from a CSV file.
    
    Parameters:
    - file_path (str): The path to the CSV file.
    
    Returns:
    - pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    data = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
    print("Data loaded successfully")
    return data

def clean_data(data):
    """
    Clean the Brent oil prices data.
    
    Parameters:
    - data (pd.DataFrame): The raw data.
    
    Returns:
    - pd.DataFrame: The cleaned data.
    """
    # Handle missing values
    data = data.dropna()
    print("Missing values removed")

    # Reset index
    data = data.reset_index(drop=True)
    print("Index reset")
    
    return data

if __name__ == "__main__":
    file_path = '../data/brent_oil_prices.csv'
    data = load_data(file_path)
    clean_data = clean_data(data)
    print(clean_data.head())