import re

def findNumbera_Instring(input1):
    pattern='\d+'
    numbers=re.findall(pattern,input1)
    return numbers


input1="there are 3434 boxes 3 pencils 233 Pens"
numbers=findNumbera_Instring(input1)
print(numbers)
