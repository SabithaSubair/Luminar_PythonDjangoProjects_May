num=int(input("Limit:"))

for i in range(0,num):
    for j in range(num,i,-1):
         print("*",end=" ")
    print("\r")

print("another method using function")
def pattern(row):
    for i in range(row,0,-1):
        for j in range(0,i):
            print("*", end=" ")
        print("\r")
pattern(6)