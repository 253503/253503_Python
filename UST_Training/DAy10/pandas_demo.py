import pandas as pd


name=pd.Series(['Virat','Dhoni'])
team=pd.Series(['RCB','CSK'])
dic={'Name':name,'Team':team}
df=pd.DataFrame(dic,index=['RANK2','RANK1'])

#df=pd.DataFrame(dic)
#print(df)

#type:1
#for row in df.iterrows():
#    print(row)
#    break

#type 2
# for row_index,row_value in df.iterrows():
#     print("--------")
#     print("row index is:",row_index)
#     print("row Value is:",row_value)

for col_index,col_value in df.iteritems():
    print("--------")
    print("col index is:",col_index)
    print("col Value is:",col_value)