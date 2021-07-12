def rev_parallellogram(n):
    k=n

    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")

        k=k-1
        for j in range(0,r):
            print("*", end=" ")
        print("\r")
rev_parallellogram(5)