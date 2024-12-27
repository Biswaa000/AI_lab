#  19) Define classes Engine, Wheel, and Car. Engine and Wheel classes have attributes type and
#  methods start() and stop(). The Car class should have instances of Engine and Wheel classes
#  as attributes. Implement a method start_car() in the Car class which starts the engine and prints
#  "Car started".

class Engine:
    def __init__(self,engine_type):
        self.type=engine_type

    def start(self):
        print(f"{self.type} engine started.")

    def stop(self):
        print(f"{self.type} engine stopped.")



class Wheel:
    def __init__(self,wheel_type):
        self.type= wheel_type

    def start(self):
        print(f"{self.type} engine started.")

    def stop(self):
        print(f"{self.type} engine stopped.")

class Car:
    def __init__(self,engine_type,wheel_type):
        self.engine=Engine(engine_type)
        self.wheel=Wheel(wheel_type)
        
    def start(self):
        self.engine.start()
        print("carr started....")

my_car = Car("V8", "Alloy_rubber")
my_car.start() 