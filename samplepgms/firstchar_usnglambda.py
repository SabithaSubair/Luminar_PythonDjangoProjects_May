#hello.......h
#good.....g
print("normal program")
def print_firstchar(word):
    return word[0]
print(print_firstchar("hello"))
print("using lambda")
first=lambda char:char[0]
print(first("good"))
print("remove last element")
lst=[1,2,3,4]
lst.pop()#remove last element
print(lst)