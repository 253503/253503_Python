import pandas as pd


name=pd.Series(['Virat','Dhoni'])
team=pd.Series(['RCB','CSK'])
dic={'Name':name,'Team':team}
df=pd.DataFrame(dic)


print(df)
df.columns=['New Name','New Team']
print(df)