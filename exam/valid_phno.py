import re
n=input("enter the word to validate")
x='^[A-Z][a-zA-Z0-9][A-Z]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")