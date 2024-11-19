import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"

#lets try the get method

response = requests.get(url)

if(response.status_code ==200):
    print("Everything went well")
    print(response.json())
else:
    print("something went wrong",str(response.status_code))

df = pd.DataFrame(response.json())
print(df)