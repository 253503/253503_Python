import re
pattern = "^a...s$"
test_string="abyss"
result=re.match(pattern,test_string)
if result:
    print("success")
else:
    print("no match")