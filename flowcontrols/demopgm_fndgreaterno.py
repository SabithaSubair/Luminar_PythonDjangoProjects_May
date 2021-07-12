print("find greater of 2 no")
n1=int(input("enter your no1:"))
n2=int(input("enter your no2:"))
if(n1>n2):
    print("Number 1 is greater")
elif n1==n2:
    print("Equal number")
else:
    print("Number 2 is greater")

print("greater of 3 number")
no1=int(input("enter your no1:"))
no2=int(input("enter your no2:"))
no3=int(input("enter your no3:"))
if(no1>no2 & no1>no3):
    print("Number 1 is greater")
elif no2 > no2 & no2 > no3:
    print("Number 2 is greater")
# elif (no2 > no2) and ( no2 > no3): ...also use for this method
#     print("Number 2 is greater")
elif no1==no2==no3:
    print("Equal")
else:
    print("Number 3 is greater")