import requests

url = "https://httpbin.org/headers"
headers={"Custom_Header":"Gayathri's value"}

response = requests.get(url,headers=headers)

print(response)
print(type(response))
print(response.headers)
print(response.json())
