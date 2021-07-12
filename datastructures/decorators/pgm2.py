def swap(func):
    def wrapper(num1,num2):
        num1,num2=num2,num1
        return func(num1,num2)
    return wrapper

@swap
def sub(num1,num2):
    return num1-num2
print(sub(5,10))