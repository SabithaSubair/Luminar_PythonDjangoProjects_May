# 1
# 1 2
# 1 2 3
print("first method")
num=int(input("Limit:"))
for i in range(1,num+1):

    for j in range(1,i+1):

         print(j,end=" ")
    print("\r")

print("another method")
num=int(input("Limit:"))
c=0
for i in range(0,num):
    c=0
    for j in range(0,i+1):
         c=c+1
         print(c,end=" ")
    print("\r")
