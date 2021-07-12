lst=[1,2,3,4,5,6,7]
lst_mul = []
for i in lst:
        mul=i*5
        lst_mul.append(mul)
print("Multiple of element is:",lst_mul)
#another method..more effective bcoz less coding steps...
#called list comprehension
print(" using list_comprehension")
a=[1,2,3,4,5]
b=[i*5 for i in a]
print(b)
print("using list_comprehension with if condn")
c=[1,2,3,4,5]
d=[i*5 for i in c if i>2]
print(b)