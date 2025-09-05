from pandas import DataFrame, isna, get_dummies
# from numpy import NaN

# df = DataFrame({
#     'C1': [1, 2, 3, None],
#     'C2': [4, 5, 6, None],
#     'C3': [7, 8, 9, None],
#     'C4': [10, 11, None, 12]
# })
# mean=df.mean()
# df = df.fillna(mean)
# print(df, mean)
# import pandas as pd

data = {'Name': ['John', 'Cateline', 'Matt', 'Oliver'],
        'ID': [1, 22, 23, 36]}

df = DataFrame(data)

#one hot encoding 
new_df = get_dummies(df.Name)
print(new_df.head())