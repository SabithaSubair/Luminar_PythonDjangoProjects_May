class Operators:
  def num(self,a,b):
      self.a=a
      self.b=b
      print("parent",self.a+self.b)
  def num(self,c,d):
      self.c=c
      self.d=d
      print("child",self.c*self.d)
o=Operators()
o.num(1,2)#error
