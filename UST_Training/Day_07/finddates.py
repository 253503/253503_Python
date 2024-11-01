import re

pattern = r'\b\d{4}-\d{2}-\d{2}|\b\d{4}/\d{2}/\d{2}'
input1='I have work on 2024-02-02 and also on 2024/03/08'
print(input1)
dates=re.findall(pattern,input1,re.IGNORECASE)
print(dates)
