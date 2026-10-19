import pandas as pd

#We are gonna practice pandas and dataframes

db = pd.read_csv("data.csv")
df = pd.DataFrame(db)

df.head()
df.aggregate({'column_name': 'sum'})  # Replace 'column_name' with the actual column you want to aggregate  
df.describe()  # Get summary statistics for the DataFrame
df.info()  # Get information about the DataFrame, including data types and non-null counts
df.isnull().sum()  # Check for missing values in each column
df['new_column'] = df['existing_column'] * 2  # Create a new column based on an existing column
df.sort_values(by='column_name', ascending=False)  # Sort the DataFrame by a specific column
df.groupby('group_column').mean()  # Group by a column and calculate the mean for each group    
df.dropna()  # Drop rows with missing values
df.fillna(0)  # Fill missing values with a specified value (e.g., 0)
df.to_csv("output.csv", index=False)  # Save the DataFrame to a new CSV file without the index

df.head()
df.aggregate({'max_colmn': 'max'})  # Replace 'max_column' with the actual column you want to find the maximum value for    


def read_csv():
    db = pd.read_csv("data.csv")
    df = pd.DataFrame(db)
    return df
def write_csv(df):
    df.to_csv("output.csv", index=False)
    return "DataFrame saved to output.csv"
def extract_column(df, column_name):
    if column_name in df.columns:
        return df[column_name]
    else:
        return f"Column '{column_name}' does not exist in the DataFrame."
def filter_rows(df, column_name, value):
    if column_name in df.columns:
        return df[df[column_name] == value]
    else:
        return f"Column '{column_name}' does not exist in the DataFrame."   

def group_by_and_aggregate(df, group_column, agg_column, agg_func):
    if group_column in df.columns and agg_column in df.columns:
        return df.groupby(group_column)[agg_column].agg(agg_func)
    else:
        return f"One or both columns '{group_column}' and '{agg_column}' do not exist in the DataFrame."
def sort_dataframe(df, column_name, ascending=True):
    if column_name in df.columns:
        return df.sort_values(by=column_name, ascending=ascending)
    else:
        return f"Column '{column_name}' does not exist in the DataFrame."
def drop_missing_values(df):
    return df.dropna()
def fill_missing_values(df, value):
    return df.fillna(value)
def get_summary_statistics(df):
    return df.describe()
def get_dataframe_info(df):
    return df.info()
def check_missing_values(df):
    return df.isnull().sum()
def create_new_column(df, new_column_name, existing_column_name, operation): 


    if existing_column_name in df.columns:
        if operation == 'multiply':
            df[new_column_name] = df[existing_column_name] * 2
        elif operation == 'add':
            df[new_column_name] = df[existing_column_name] + 2
        elif operation == 'subtract':
            df[new_column_name] = df[existing_column_name] - 2
        elif operation == 'divide':
            df[new_column_name] = df[existing_column_name] / 2
        else:
            return f"Operation '{operation}' is not supported."
        return df
    else:
        return f"Column '{existing_column_name}' does not exist in the DataFrame."
    