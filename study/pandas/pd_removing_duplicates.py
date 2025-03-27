import pandas as pd

csv = 'datalab.csv'
df = pd.read_csv(csv)

print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df.duplicated())