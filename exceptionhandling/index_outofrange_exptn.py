# print("normal case")
# a=[1,2,3,4]
# print(a[5])
#....output is below:
# print(a[5])
#IndexError: list index out of range
#solution
print("index out of range")
lst=[1,2,3,4,5,6]
index = int(input("enter the index:"))
try:
    print(lst[index])
except Exception as e:
    print("exception is:-",e)
finally:
    print("inside finally")

