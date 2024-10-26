def oddeven(x):
    if(x%2==0):
        return "even"
    else:
        return "odd"
print(oddeven(6))

print("what is your input number")
user_input=int(input())
x=oddeven(user_input)
print("answer is"+x)
#print("what is your input number")
#user_input=input()
#print("your input is"+user_input)