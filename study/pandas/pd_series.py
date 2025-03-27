import pandas as pd

a = [13,2,5,24]

# myvar= pd.Series(a) # Pandas Series is like a column in a table.
# print(myvar)
# print(myvar[0]) # show the num/value at the index 0



myvar = pd.Series(a, index = ["w","x", "y", "z"]) #defining a index to our value on set  

print(myvar["y"])
print(myvar["z"]) # show the num/value at the index "y" and "z"