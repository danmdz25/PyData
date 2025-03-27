import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390} #The keys of the dictionary become the labels.
myvar = pd.Series(calories)
print(myvar)