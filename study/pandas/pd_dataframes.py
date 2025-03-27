import pandas as pd
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.
workout_data = {
    "name":['Daniel','Elo','Vivi'],
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(workout_data)

print(myvar.loc[[0,1]])