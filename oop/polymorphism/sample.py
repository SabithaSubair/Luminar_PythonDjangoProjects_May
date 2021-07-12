#polymorphism.....means many forms
#same method multiple times use
#overloading..means same method name and deff no of args...not supported in python
#over_riding
class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
class Display(Operators):
    def num(self,n3):
        self.n3=n3
        print(n3)
d=Display()
d.num(3,2)#out is error..becoz of this method.just know the concept only.....out is:Traceback (most recent call last):
# d.num(3,2)
#TypeError: num() takes 2 positional arguments but 3 were given
#so only support to call recent function ie one argument

d.num(3)#out is 3
#overloading is not supported in python