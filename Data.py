import pandas as pd

file_path = 'report_2_.csv'
column_names = ['Week', 'data science', 'data scientist', 'analytics', 'google analytics', 'machine learning']
data = pd.read_csv(file_path, skiprows=4, names=column_names)
data = data.drop(0)

for column in column_names[1:]:
    data[column] = pd.to_numeric(data[column])
correlation_matrix = data.corr()
print(correlation_matrix)
correlation = correlation_matrix['data science']['data scientist']
correlation_percentage = correlation * 100
print(correlation_percentage)
