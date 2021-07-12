num1=int(input("enter number1"))
num2=int(input("enter number2"))
try:
    print("hello")
    print(num1/num2)
except Exception as e:
    print("exception occured",e)
finally:
    print("inside finally")
    