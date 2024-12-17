class Circle:
    def __init__(kucho,radius):
        kucho.radius=radius
    def __str__(kucho):
        print(" this call when we try to print obj of class")

    def area(kucho):
        return 3.1415*(kucho.radius**2)
    def perimeter(kucho):
        return 2 * 3.1415 * kucho.radius
        
    
c1=Circle(5)
area=c1.area()
perimeter=c1.perimeter()
print(area,perimeter)