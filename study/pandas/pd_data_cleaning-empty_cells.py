import pandas as pd

csv='datalab.csv'

df = pd.read_csv(csv)

# print(df.to_string())

# new_df = df.dropna()

# print(new_df.to_string())

# df.dropna(inplace = True) # remove rows that contain empty cells

# print(df.to_string())

# df.fillna(111,inplace=True) # replace empty values
# print(df.to_string())
df['Calories'].fillna(111,inplace=True) # specific column empty values replace
print(df.to_string())

