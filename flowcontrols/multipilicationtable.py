print("using for loop")
n=int(input("enter your no:"))
for i in range(1,11):
    print(i,"*",n,"=",n*i)

print("using while loop")
i=1
while i<=10:
    res=i*n
    print(i,"*",n,"=",res)
    i+=1