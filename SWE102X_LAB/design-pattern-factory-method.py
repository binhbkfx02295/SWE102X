from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self):
        product = self.factory_method() 
        result = f"Creator: the Creator's code has just worked with: {product.operation()}"
       
        return result
    
    
class ConcreteCreator1(Creator):
    
    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):
    
    def factory_method(self) -> Product:
        return ConcreteProduct2()

class Product(ABC):
    
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"
    
def client_code(creator: Creator) -> None:
    print(creator.some_operation())
    pass

if __name__ == "__main__":
    client_code(ConcreteCreator1())
    
    print()
    
    client_code(ConcreteCreator2())
