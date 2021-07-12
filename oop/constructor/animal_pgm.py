class Animal:
    def __init__(self,category,color,type):#attributes
        self.category=category#instance variable
        self.color=color
        self.type=type
class Dog(Animal):
    def printval(self):
        print("category::",self.category)
        print("color::",self.color)
        print("type::",self.type)
obj1=Dog("Dog","brown","German_Shepherd")
obj1.printval()

