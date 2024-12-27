
#  16) Define a class Vehicle with attributes make and model, and a method drive() which prints
#  "Driving the [make] [model]". Then, create a subclass Car that inherits from Vehicle and overrides
#  the drive() method to print "Driving the [make] [model] car".

class Vehile:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    
    def __str__(self):
        pass

    def drive(self):
        print(f"p-Driving the {self.make}-{self.model}")

class Car(Vehile):
    def drive(self):
        print(f"c-Driving the {self.make}-{self.model}")

bike=Vehile("Honda","312h")
bike.drive()
car=Car("BMW","bs009")
car.drive()