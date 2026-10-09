#Create ETL pipeline to extract data from a CSV file, transform it, and load it into a database.
import pandas as pd
import sqlite3

def extract_data(file_path):
    """Extract data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        print("Data extraction successful.")
        return data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None
def transform_data(data):
    """Transform the extracted data."""
    try:
        # Example transformation: drop rows with missing values
        transformed_data = data.dropna()
        print("Data transformation successful.")
        return transformed_data
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None
def load_data(data, db_path, table_name):
    """Load the transformed data into a database."""
    try:
        conn = sqlite3.connect(db_path)
        data.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        print("Data loading successful.")
    except Exception as e:
        print(f"Error loading data: {e}")

def etl_pipeline(file_path, db_path, table_name):
    """Run the ETL pipeline."""
    data = extract_data(file_path)
    if data is not None:
        transformed_data = transform_data(data)
        if transformed_data is not None:
            load_data(transformed_data, db_path, table_name)
if __name__ == "__main__":
    # Define file path, database path, and table name
    csv_file_path = 'data.csv'  # Path to your CSV file
    database_path = 'database.db'  # Path to your SQLite database
    table_name = 'my_table'  # Name of the table to load data into

    # Run the ETL pipeline
    etl_pipeline(csv_file_path, database_path, table_name)