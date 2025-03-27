import pandas as pd 

csv= 'datalab.csv'

df = pd.read_csv(csv)

x= df['Calories'].mean() # mean value x.sum()/x.len()
y= df['Calories'].mode() # mode the value that appears most frequently
z= df['Calories'].median() # median the value in the middle, after you have sorted all values ascending. [1,2,{3},4,5]

df.fillna(x,inplace=True)
print(x)
print(y)
print(z)
# print(df.to_string)