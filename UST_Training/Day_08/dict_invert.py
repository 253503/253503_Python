data={'a':1,'b':2,'c':3}

new_data={}

for key in data:
        print(key)
        value=data[key]
        print(value)
        new_data[value]=key
print(new_data)