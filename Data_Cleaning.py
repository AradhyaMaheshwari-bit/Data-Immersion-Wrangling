"""
ApexPlanet Internship - Task 1
Data Immersion & Wrangling

Author: Aradhya Maheshwari
Description:
This script performs data cleaning and preprocessing on the ApexPlanet
Data Analytics dataset using Python and Pandas.
"""

import pandas as pd

# Load the dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# -----------------------------
# 1. Display basic information
# -----------------------------
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# 2. Check Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill missing City with mode
df['City'] = df['City'].fillna(df['City'].mode()[0])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# -----------------------------
# 3. Convert Order_Date to Date
# -----------------------------
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# -----------------------------
# 4. Check Duplicate Rows
# -----------------------------
print("\nDuplicate Rows:", df.duplicated().sum())
print("\nDuplicate Order IDs:")
print(df['Order_ID'].duplicated().sum())

# -----------------------------
# 5. Verify Total Sales
# -----------------------------
df['Calculated_Sales'] = df['Quantity'] * df['Unit_Price']

print("\nSales Verification:")
print((df['Calculated_Sales'].round(2) == df['Total_Sales'].round(2)).value_counts())

# -----------------------------
# 6. Create New Features
# -----------------------------
df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Quarter'] = df['Order_Date'].dt.quarter
df['Day_Name'] = df['Order_Date'].dt.day_name()

# Remove helper column
df.drop(columns=['Calculated_Sales'], inplace=True)

# -----------------------------
# 7. Save Cleaned Dataset
# -----------------------------
df.to_excel("Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx", index=False)

print("\nData cleaning completed successfully!")
print("Cleaned dataset saved as 'Cleaned_ApexPlanet_DataAnalytics_Dataset.xlsx'")