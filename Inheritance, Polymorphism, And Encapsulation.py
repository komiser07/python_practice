import math

class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented in a subclass.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Площадь прямоугольника: {rectangle.area()}")
print(f"Площадь круга: {circle.area()}")