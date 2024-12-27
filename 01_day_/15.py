# 15) Write a Python program to create a person class. Include attributes like name, country and date of
#  birth. Implement a method to determine the person's age.
import time
class Person:
    def __init__(self,name,country,dob):
        self.name=name
        self.country=country
        self.dob=dob
    def __str__(self):
        pass

    def age(self):
        age=2024-self.dob
        
        return age

p1=Person('Bishal','Nepal',2003)
print(p1.age())