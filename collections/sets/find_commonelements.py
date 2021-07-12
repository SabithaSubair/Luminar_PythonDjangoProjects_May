s1={1,2,3,4,5,6,8,0}
s2={1,2,3,8}
common=set()
for i in s1:
    for j in s2:
        if(i==j):
            common.add(j)
print("Common Elements are:",common)
