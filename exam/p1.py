class Vehicle:

    def vehicledetails(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        print(self.name,self.max_speed,self.mileage)
class Car(Vehicle):
    def cardetails(self, model):
        self.model = model
        print(self.model)

ob=Car()
ob.cardetails("innova")
ob.vehicledetails("car",120,12)