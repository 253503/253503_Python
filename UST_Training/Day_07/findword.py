import re
# pattern = '\bs\w*'
# test_string="she sells sea shells on the sea shore"
# result=re.findall(pattern,test_string,re.IGNORECASE)

# if result:
#     print("success:",result)
# else:
#     print("no match",result) 

def findNumbera_Instring(input1):
    pattern=r'\bs\w*'
    numbers=re.findall(pattern,input1,re.IGNORECASE)
    return numbers


input1="she sells sea shells on the sea shore"
numbers=findNumbera_Instring(input1)
print(numbers)
