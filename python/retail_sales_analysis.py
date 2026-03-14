# Import pandas library for data analysis
import pandas as pd

# Load the retail sales dataset into a DataFrame
df = pd.read_csv('retail_sales.csv')

# Display the first 5 rows of the dataset
# This helps understand the structure of the data
# print(df.head())

# Show dataset information such as column names, data types, and non-null values
# Useful for identifying missing values and column types
# print(df.info())

# Generate statistical summary of numeric columns
# Includes count, mean, standard deviation, min, max, etc.
# print(df.describe())

# Check for missing values in each column
# isnull() identifies missing values and sum() counts them
print(df.isnull().sum())

# Remove rows that contain missing values
# This cleans the dataset before analysis
df = df.dropna()

# Display the shape of the dataset after cleaning
# Output format: (rows, columns)
print(df.shape)

# save cleaned dataset to data folder for SQL and Power BI
df.to_csv("../data/clean_retail_sales.csv", index=False)

# check duplicate rows in dataset
print("Duplicate rows:", df.duplicated().sum())

# calculate total revenue by product category
category_sales = df.groupby("category")["total_sale"].sum()

# display the result
print("Revenue by Category:")
print(category_sales)

# calculate total revenue by gender
gender_sales = df.groupby("gender")["total_sale"].sum()

# display the result
print("Revenue by Gender:")
print(gender_sales)

# calculate number of transactions by category
category_transactions = df.groupby("category")["transactions_id"].count()

# display the result
print("Number of Transactions by Category:")
print(category_transactions)

# save revenue by category to a csv file
category_sales.to_csv("revenue_by_category.csv")
