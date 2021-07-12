#over riding----child class method overrides parent class method
#menas same method name and same no of argmnts
class Person:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def printval(self,cls):
        self.cls=cls
        print("inside child method-",self.cls)
c=Child()
c.printval("asdfgjkl")