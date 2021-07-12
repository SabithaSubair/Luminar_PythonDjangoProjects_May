a=int(input("enter the initial amount:"))
print("Initial Amount : ",a)
b=int(input("enter the withdrawal amount:"))

if(a>b):
    c=a-b
    print("Withdrawal success..Balance is:",c)
else:
    print(" You have insufficient balance")
    print(" Balance is:",a)