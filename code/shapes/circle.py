from shapes.shape import Shape
import math

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * math.pow(self.radius, 2)
