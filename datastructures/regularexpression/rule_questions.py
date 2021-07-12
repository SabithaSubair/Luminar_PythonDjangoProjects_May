#combination of uppercase and lowercase letters andending with anumber
#Abc6 fgRtggg7 sdf4 ASDR5
import re
n="Abc6"
x='^[a-zA-Z]+[0-9]$' # "[a-z][A-Z]+\d{1}$"
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")


print("from keyboard")
n = input("Enter number")
x = "[a-zA-Z]+\d$"
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")

#home work...starting with a ending with b
#eg..ab afghb a456ghkjb a#$%ghb
import re
n=input("enter number:")
x="(^a[a-zA-Z0-9\w]*b$)"
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")
