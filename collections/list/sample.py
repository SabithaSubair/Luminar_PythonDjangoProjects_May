list=[1,2,3,4,1,2,"hello",8.9,True]
# features
# 1.keep order
# 2.keep order
# 3.heterogeneous
# 4.nested lists are possible
print(list)
print(type(list))

# empty list creation
lst1=[]
print(lst1)
print(type(lst1))
#to add values in list use append
lst1.append("hai")
lst1.append(9)
print(lst1)
# nested list
lss=[1,2,[2,4,[2,9,0]]]
print(lss)
print("After seperating:")
for i in lss:
    print(i)


