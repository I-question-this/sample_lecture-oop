from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def __eq__(self, other) -> bool:
        if isinstance(other, Shape):
            return self.area() == other.area()
        else:
            return self.area() == other
 
    def __gt__(self, other) -> bool:
        if isinstance(other, Shape):
            return self.area() > other.area()
        else:
            return self.area() > other
