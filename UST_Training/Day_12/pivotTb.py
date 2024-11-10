import pandas as pd

data={
        'Store':['store1','store1','store2','store2','store3','store3','store4','store5'],
        'Region':['North','North','South','South','East','East','North','South'],
        'Sales':[200,150,300,250,400,350,100,200]
        }


df=pd.DataFrame(data)

#totalsales per store
df1=df.groupby('Store').sum()
print(df1)

#totalsales per Region
df2=df.groupby('Region').sum().reset_index()
print(df2)


#merge orginal and region dt
df3=pd.merge(df,df2,on='Region',how='left',suffixes=("_store","_region"))
print(df3)


#sales percentage of sales and region
#df=df['Store']/df['Region'] *100

df3['new column']=df2['Sales']/df3['Sales_region'] 
print(df3)