try:
    num1=int(input("input num1"))
    num2=int(input("denominator"))
    result=num1/num2
    print(result)

except ZeroDivisionError as e:
    print("you cannot divide by 0")
except Exception as e:
    print("some error happened: "+e)

print("completed")