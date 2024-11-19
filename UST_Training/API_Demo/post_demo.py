import requests

url = "https://jsonplaceholder.typicode.com/users"

#lets try the get method
data ={
    "title":"Gayathri","body":"hello","userId":1
}
response = requests.post(url,json=data)
print(response.status_code)