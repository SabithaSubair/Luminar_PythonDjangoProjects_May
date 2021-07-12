class Vehicle:
    def vehicle_details(self,vehicle_model,reg_no,color):
        self.vehicle_model=vehicle_model
        self.reg_no=reg_no
        self.color=color
class Bus(Vehicle):
    def setval(self,type):
        self.type=type
        print("Type::",self.type)
        print("Model::",self.vehicle_model)
        print("Reg_no::",self.reg_no)
        print("Color::",self.color)
obj=Bus()
obj.vehicle_details("bus",30,"blue")
obj.setval("private")


