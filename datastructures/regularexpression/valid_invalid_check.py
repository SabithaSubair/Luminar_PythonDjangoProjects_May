import re
n="hello"
x='\w*'
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")

print("56kg....print")
n='56kg'
x='[0-9]{2}[k][g]' #or '[0-9]{2}[a-z]{2}'
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")
