class Person:
    def persondetails(self, name, age):
        self.name = name
        self.age = age
        print(self.name, self.age)


class Parent(Person):
    def parentdetails(self, address):
        self.address = address
        print(self.address)


class Employee(Parent):
    def empdetails(self, id, designation, salary):
        self.id = id
        self.designation = designation
        self.salary = salary
        print(self.id, self.salary, self.designation)
pa=Parent()
pa.parentdetails("zxc")
pa.persondetails("asdfcvb",20)

em = Employee()
em.empdetails(101, 1000, "accountant")
em.parentdetails("asdd")
em.persondetails("asd", 20)

