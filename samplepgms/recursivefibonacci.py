def recursive_fibonaaci(n):
    if n<=1:
        return n
    else:
        return recursive_fibonaaci(n-1)+recursive_fibonaaci(n-2)
num=int(input("Enter number:"))
if num==0:
    print("Please enter a positive integer")
else:
    print("Fibonacci series is:")
    for i in range(num):
        print(recursive_fibonaaci(i))