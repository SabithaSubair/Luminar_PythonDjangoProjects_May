def trapizoid(n):
    k=n

    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k=k-1
        for j in range(0,i+5):
            print("*", end=" ") #0,1,2
        print("\r")
trapizoid(5)
