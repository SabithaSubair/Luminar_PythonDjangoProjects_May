#multilevel or heirarchical inheritance
class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age

        print(self.name,self.age)
class Child(Person):
    def cvalue(self,address,cls):
        self.address = address
        self.cls=cls
        print(self.address,self.cls)
class Student(Child):
    def svalue(self, rolno, mark):
        self.rolno = rolno
        self.mark = mark
        print(self.rolno, self.mark)
ch=Child()
ch.cvalue("asd",6)
ch.pvalue("anu",24)

st=Student()
st.svalue(4,78)
st.cvalue("amal",9)
st.pvalue("arun",25)
