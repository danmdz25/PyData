import pandas as pd

csv='data_ts.csv'

df = pd.read_csv(csv)
numb_list=[]
rep_numb_list=[]
for x in df.index:
    if df.loc[x,'Telefone'] not in numb_list:
        numb_list.append(df.loc[x,'Telefone'])
    else:
        print(f'O número: {df.loc[x,'Telefone']} já entrou em contato antes do dia: {df.loc[x,'Data']}' )
        rep_numb_list.append(df.loc[x,'Telefone'])
        df.drop(x,inplace=True)

# print(df.to_string())
# for x in rep_numb_list:
#     if x in numb_list:
#         print(f"O número {x} se repete")
# print(rep_numb_list.__len__())