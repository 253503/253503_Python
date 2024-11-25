import requests

url="https://api.coingecko.com/api/v3/simple/price"
params = {"ids":"bitcoin",}

response = requests.get(url,params)
print(response)
for item in range(100):
    if(response.status_code ==200):
        print("everything ok")
    elif(response.status_code==429):
        print("rate limit exceeded")
        time.sleep(60)
    else:
         print("its failing due to unknown reason")
