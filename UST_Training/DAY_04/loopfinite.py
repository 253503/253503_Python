import random

count=1
while True:
    print("help!")
    if random.choice(range(1000))==111:
        break
    print('let me out!')
    
    count+=1
    print(count)
print('At Last escape')

