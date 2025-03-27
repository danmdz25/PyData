import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2],
  'value':['R$ 300.000','R$ 450.000','R$ 150.000']
}

myvar = pd.DataFrame(mydataset)


print(myvar)
# print(pd.__version__)
