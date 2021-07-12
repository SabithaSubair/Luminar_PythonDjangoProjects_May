def fact(x):
    #this is recursive factorial fn
    if x==1:
        return 1
    else:
        return (x * fact(x-1))
n= int(input("enter no:"))
print("Factorial:",n,"is",fact(n))
