#oop is used to code is more effective
#code re-usability
#concept :..
#class..design pattern/structure or blueprint
#object...real world entity
#reference...to perform oprations on object
#eg: tv..calss, object..defferent companies...reference...remote
# eg2:student..class,object..every students

class Person:#rules:1..class name start with capital letter followed by ':'
     def walk(self):#method1#object..self is instane keyword..automatically came..only inside a function
         print("person is walking")
     def read(self):#methods2.#.inside class function called methods..here two methods
         print("person is reading")
obj1=Person() #create reference..obj1 is reference
obj1.walk()
obj1.read()
obj2=Person()
obj2.walk()
obj2.read()