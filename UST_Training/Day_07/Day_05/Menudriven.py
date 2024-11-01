def arithmetic_operations(a,b,operation_type):
    if(operation_type=='add'):
        return a+b
    elif(operation_type=='sub'):
        return a-b
    elif(operation_type=='mul'):
        return a*b


input_Num=''
while (input_Num !='4'):
    print("1.Add two numbers\n 2.Subtract two numbers\n3.Multiply two numbers\n4.Quit")
    input_Num=input("Enter your choice")

    if(input_Num=='1'):
        a=int(input("Enter number a:"))
        b=int(input("Enter number b:"))
        print('a+b',arithmetic_operations(a,b,operation_type='add'))
    elif(input_Num=='2'):
        a=int(input("Enter number a:"))
        b=int(input("Enter number b:"))
        print('a-b',arithmetic_operations(a,b,operation_type='sub'))
    elif(input_Num=='3'):
        a=int(input("Enter number a:"))
        b=int(input("Enter number b:"))
        print('a*b',arithmetic_operations(a,b,operation_type='mul'))
