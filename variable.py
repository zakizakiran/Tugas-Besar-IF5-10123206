import pandas as pd

# Load data
data1 = pd.read_csv('dataset/day.csv')
data2 = pd.read_csv('dataset/hour.csv')

# Pastikan kolom memiliki kesamaan sebelum menggabungkan
common_columns = list(set(data1.columns) & set(data2.columns))
combined = pd.concat([data1, data2], ignore_index=True, sort=False)

# Cek missing values sebelum mengisi
missing_values = combined.isnull().sum()

# Hanya isi missing values untuk kolom yang relevan
if 'hr' in combined.columns:
    combined['hr'].fillna(combined['hr'].mean(), inplace=True)

# Data setelah cleaning
cleaned_data = combined