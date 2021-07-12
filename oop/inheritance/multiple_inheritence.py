#multiple inheritence
class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age

        print(self.name,self.age)
class Child:
    def cvalue(self,address,cls):
        self.address = address
        self.cls=cls
        print(self.address,self.cls)

class Student(Person,Child):
    def svalue(self,rolno,mark):
        self.rolno=rolno
        self.mark=mark
        print(self.rolno,self.mark)
st=Student()
st.pvalue("asd",20)
st.cvalue("aasdd",9)
st.svalue(101,50)
