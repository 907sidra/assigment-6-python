from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Example Usage
if __name__ == "__main__":
    rect = Rectangle(5, 4)
    print("Area of Rectangle:", rect.area())
