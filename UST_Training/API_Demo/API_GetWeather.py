import requests

url = "https://api.open-meteo.com/v1/forecast"
params ={
    "latitude":12.9719,
    "longitude":77.5937,
    "current_weather":"true"
        }


# response = requests.get(url,params)

# print(response.json()['current_weather'])

for item in range(100):
    print("iteration",item)
    response = requests.get(url,params)
    print(response)

    if(response.status_code ==200):
        print("everything ok")
    elif(response.status_code==429):
        print("rate limit exceeded")
        time.sleep(60)
    else:
         print("its failing due to unknown reason")
         
