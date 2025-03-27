import pandas as pd

csv='datalab.csv'
df = pd.read_csv(csv)

print(df.corr())