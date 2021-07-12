# no1=2
# no2=4
no1=int(input("enter the 1st num:"))
no2=int(input("enter the 2nd num:"))
print("Before swapping:",no1,no2)
temp=no1
no1=no2
no2=temp
print("After swapping:",no1,no2)

#2nd approach
print("second approach")
(no1,no2)=(no2,no1)
print("after swap",no1,no2)
#thirdapproach
print("3rd approach")
no1=no1+no2
no2=no1-no2
no1=no1-no2
print("after swap",no1,no2)