# polymorphism_demo.py
import math

class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    