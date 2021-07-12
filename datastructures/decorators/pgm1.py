def check(func):#can change check and func nale theses are varibale names
    def wrapper(name,age):#can chage wrapper it is a variable name
        if age<18:
            print(name,"-->not eligible")
        else:
            return func(name,age)
    return wrapper

@check
def vaccine(name,age):
    print(name,"-->eligible")
vaccine("anu",19)
vaccine("seetha",17)