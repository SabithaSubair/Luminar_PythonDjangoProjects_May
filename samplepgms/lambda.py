#lambda...use this keyword
#to reduce code
#lambda function in functional programming
# def cube(num):
#     return num**3
# print(cube(3)).....................//normal program
#using lambda function
print("cube")
a=lambda num:num**3
print(a(7))
print(a(2))
print("addition")
add=lambda num1,num2:num1+num2
print(add(10,10))
print("input from keyboard")
addn=lambda n1,n2:n1+n2
n1=int(input("enter number1:"))
n2=int(input("enter number2:"))
print(add(n1,n2))
