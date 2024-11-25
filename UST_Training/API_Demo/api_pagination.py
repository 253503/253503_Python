import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {"_page":1,"_limit":5}

response = requests.get(url,params)
print(len(response.json()))
