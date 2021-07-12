class Operators:
  def num(self,a,b):
      self.a=a
      self.b=b
      print(self.a+self.b)
  def num(self,c):
      self.c=c
      print(self.c)
o=Operators()
o.num(1,2)#error
o.num(1)