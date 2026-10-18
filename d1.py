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

 