#model,regno,color

class Vehicle:
    def vehicle(self,vehicle_model,reg_no,color):
        self.vehicle_model=vehicle_model
        self.reg_no=reg_no
        self.color=color

        print(self.vehicle_model,self.reg_no,self.color)

    #two string method--->convertg our obj to a string
    def _str_(self):
        return self.vehicle_model
v=Vehicle()
v.vehicle("KTM","KL44A123","blue")
print(v)# without two string we will get the location address, after adding the two string we will get the value given in the two string method
#used in Django
