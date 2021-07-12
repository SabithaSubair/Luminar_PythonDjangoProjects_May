# prime number in a range

min=int(input("enter initial range"))
max=int(input("enter final range"))
for a in range(min,max):
    if a>1:
         for i in range(2,a):
             if(a % i) == 0:
                 break
         else:
             print(a)
#sum of prime number in a range

min=int(input("enter initial range"))
max=int(input("enter final range"))
sum=0
for a in range(min,max):
    if a>1:
         for i in range(2,a):
             if(a % i) == 0:
                 break
         else:
             print(a)
             sum=sum+a
print("sum=",sum)