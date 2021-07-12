limit=int(input("Enter limit:"))
s=set()
for i in range(limit):
    num=int(input("enter element to add:"))
    s.add(num)
print("Elements in set are:",s)