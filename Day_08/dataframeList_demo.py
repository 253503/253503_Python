import pandas as pd

dic={'a':['1','3'],'b':['2','4']
    }

input1='';
while (input != '3'):
    print("Please enter the choice:\n 1.Add to Dictionary\n 2.Display DataFrame\n 3. Exit")
    input1=input()
    if(input1=='1'):
        print("Enter key to add:")
        key=input()
        print("ENter value to add:")
        value=input()
        dic[key]=value.split(',')
    elif(input1=='2'):
        df=pd.DataFrame(dic)
        print(df)
