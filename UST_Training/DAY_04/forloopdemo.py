def username(name,x):
    """return the name for n times"""
    for i in range(x):
        print(name)
    
print("what is your name")
user_input=input()
print("ENter x value")
print("Display")
user_range=int(input())
username(user_input,user_range)
