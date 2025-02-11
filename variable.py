import pandas as pd

data1 = pd.read_csv('Datasepeda/day.csv')
data2 = pd.read_csv('Datasepeda/hour.csv')

combined = pd.concat([data1, data2], ignore_index=True)

combined.fillna({'hr': combined['hr'].mean()}, inplace=True)

cleaned_data = combined