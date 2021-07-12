class Teacher:
    def printval(self,name,subject):
        self.name=name
        self.subject=subject
        print("inside teacher method",self.name,self.subject)
class Child(Teacher):
    def printval(self,cls):
        self.cls=cls
        print("inside child method-",self.cls)
c=Child()
c.printval("10th_class")