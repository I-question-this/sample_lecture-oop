#!/bin/env python3
from shapes.rectangle import Rectangle
from shapes.circle import Circle


rect = Rectangle(4, 5)
print(f"rect area: {rect.area()}")

rect2 = Rectangle(3,8)
print(f"rect2 area: {rect2.area():.2f}")

print(f"rect.area() > rect2.area(): {rect.area() > rect2.area()}")

circ = Circle(3)
print(f"circ area: {circ.area():.2f}")

print(f"circ.area() > rect.area(): {circ.area() > rect.area()}")


print(f"rect > rect2: {rect > rect2}")
print(f"circ > rect: {circ > rect}")
