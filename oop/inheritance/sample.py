class Person:
    def pdetails(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(self.name,self.age,self.address)
class Student(Person):
    def sdetails(self,rolno,deprtmnt,mark):
        self.rolno=rolno
        self.deprtmnt=deprtmnt
        self.mark=mark
        print(self.rolno,self.deprtmnt,self.mark)
        print(self.name,"Mark is:",self.mark)
st=Student()
st.pdetails("anu",24,"asddf")
st.sdetails(1,"cs",89)
