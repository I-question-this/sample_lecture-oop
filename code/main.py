#!/bin/env python3
from shapes.rectangle import Rectangle
from shapes.circle import Circle


circ = Circle(3)
print(f"circ area: {circ.area():.2f}")

circ2 = Circle(5)
print(f"circ2 area: {circ2.area():.2f}")

print(f"circ.area() > circ2.area(): {circ.area() > circ2.area()}")

rect = Rectangle(4, 5)
print(f"rect area: {rect.area()}")

print(f"circ.area() > rect.area(): {circ.area() > rect.area()}")


print(f"circ > circ2: {circ > circ2}")
print(f"circ > rect: {circ > rect}")
