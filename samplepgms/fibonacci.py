# 0 1 1 2 3 5 8

n1=0
n2=1
a=int(input("Enter the limit:"))
print("Fibonnacci")
for i in range(a):
    print(n1)
    sum=n1+n2
    n1=n2
    n2=sum

#using while

print("Using while")
nterms=10
n1=0
n2=1
count=0
print("fibonacci sequence")
while count < nterms:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count +=1
