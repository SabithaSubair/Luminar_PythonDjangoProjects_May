tuple=(1,2,3,4,5)
print(tuple)
print(type(tuple))
print("empty tuple")
tuple2=()
print(tuple2)
tuple3=1,2,3,5 # not necessary for ()
print(tuple3)
print(type(tuple3))
#   .......features.............
#immutable...updation is not posiibble and not remove
#heterogeneous
#indexing possible
#not update and remove
print("heterogenous")
t="hai",1,8.9
print(t)
print("indexing")
print("first index:",tuple[1])
print("last index:",tuple[-1])

# to find max vale and min value
print("min value:",min(tuple),"\n","Max value:",max(tuple),"\n","Lenght is:",len(tuple))
