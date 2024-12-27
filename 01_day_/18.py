#  18) Implement a class Shape with a method area() which returns 0. Then, create subclasses
#  Rectangle and Circle. Overload the area() method in both subclasses to calculate and return
#  the area of a rectangle and a circle respectively.

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f"the area of rectangle is {self.l*self.b}")

class Circle(Shape):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        print(f"the area of cirlce is {3.14*self.r*self.r}")

r1=Rectangle(4,5)
r1.area()
c1=Circle(4)
c1.area()