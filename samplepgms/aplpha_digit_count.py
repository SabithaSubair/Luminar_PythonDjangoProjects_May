a=input("Enter string:")
b="abcdefghijklmnopqrstuvwwxyz"
c="1234567890"

d=0
e=0

for i in a:
    if i in b:
        d = d + 1
    elif i in c:
        e = e + 1
print("Count of alphabet is: ",d)
print("Count of number is: ",e)