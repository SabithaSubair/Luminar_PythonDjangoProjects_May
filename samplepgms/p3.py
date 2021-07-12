a=int(input("initial range:"))
b=int(input("final range:"))
# num=int(input("Limit:"))

for i in range(a,b):

    for j in range(0,i+1):

         print("1",end=" ")
    print("\r")
for i in range(b,a,-1):

    for j in range(0,i):

         print("2",end=" ")
    print("\r")
