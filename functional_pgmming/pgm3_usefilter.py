lst=[1,2,3,4,5,6,7]# out is:[2, 4, 6]

#print even numbers only
#filter(function,iterable)
evens=list(filter(lambda num:num%2==0,lst))
print("even numbers:",evens)
#print odd numbers
odds=list(filter(lambda num:num%2 !=0,lst))
print("odd numbers:",odds)
print("hello")
