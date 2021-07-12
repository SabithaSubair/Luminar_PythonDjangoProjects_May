


# a="Luminar"
# b=input("Enter the element to be search:")
# if b in a:
#     print("present")
# else:
#     print("not present")


#another method
a="Luminar"
b=input("Enter the element to be search:")
flag=0
for i in a:
    if i in b:
        flag=1
if flag==1:
    print("present")
else:
    print("not present")