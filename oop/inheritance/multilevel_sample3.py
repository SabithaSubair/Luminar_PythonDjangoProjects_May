class Person:
    def persondetails(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)
class Child(Person):
    def childdetails(self, address):
        self.address = address
        print(self.address)
class Parent(Person):
    def parentdetails(self,p_name,job):
        self.p_name=p_name
        self.job=job
        print(self.p_name)
        print(self.job)
class Student(Child):
    def studdetails(self,cls,mark):
        self.cls=cls
        self.mark=mark
        print(self.cls)
        print(self.mark)
c=Child()
c.childdetails("asd")
c.persondetails("as",10)
p=Parent()
p.parentdetails("xcv","accountant")
p.persondetails("sabi",30)
s=Student()
s.studdetails(10,50)
s.childdetails("adsfscfdfcd")
s.persondetails("sdfsfdsf",20)
