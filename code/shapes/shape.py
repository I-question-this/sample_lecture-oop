from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
 
    def __gt__(self, other) -> bool:
        if isinstance(other, Shape):
            return self.area() > other.area()
        else:
            raise ValueError("Can only compare with shapes")

    def __eq__(self, other) -> bool:
        if isinstance(other, Shape):
            return self.area() == other.area()
        else:
            raise ValueError("Can only compare with shapes")
