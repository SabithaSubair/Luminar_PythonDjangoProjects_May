print("normal division")
a=int(input("num1:"))
b=int(input("num2"))
c=a/b
print("divide result is:",c)

#un expected errors...use divide a num by zero
#num1:9
# num20
# Traceback (most recent call last):
#   File "C:\Users\rimna\PycharmProjects\pythonmaybatch\files\division_excptnhndling.py", line 3, in <module>
#     c=a/b
# ZeroDivisionError: division by zero
# so avoiding that method python using

#exception handling...solve un expected errors
#Using 3 blocks.."
# 1.try...exeptional code
# 2.except...solving code
# 3.finally.....anything

#division pgm using exception handling
print("exption handling")
num1=int(input("no1:"))
num2=int(input("no2:"))
try:#any time work this block
    print(num1/num2)
except Exception as e:#this block only work any exception occur
    print("exception occured..type of exception is:",e)
finally:
    print("inside finally")