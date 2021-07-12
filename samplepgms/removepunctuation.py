a=input("Enter string:")
b="abcdefghijklmnopqrstuvwwxyz1234567890"
c = ""
for i in a:
    if i in b:
        c = c + i
print("Result:",c)