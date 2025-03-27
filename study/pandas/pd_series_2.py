import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"]) # create a series using only 2 data index ('day1' and 'day2')

print(myvar) 