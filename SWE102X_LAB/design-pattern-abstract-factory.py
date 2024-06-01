from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass
    
    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass
    
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
    
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
    

class AbstractProductA(ABC):
    @abstractmethod
    def useful_method_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    
    def useful_method_a(self) -> str:
        return "Im product A1"
        
class ConcreteProductA2(AbstractProductA):
    
    def useful_method_a(self) -> str:
        return " Im product A2"

class AbstractProductB(ABC):
    @abstractmethod
    def useful_method_b(self) -> str:
        pass
    
    @abstractmethod
    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_method_b(self) -> str:
        return "The result of the product B1."
    
    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_method_a()
        return f"The result of the B1 collaborating with the ({result})"

class ConcreteProductB2(AbstractProductB):
    
    def useful_method_b(self) -> str:
        return "Im product B2"

    def another_useful_method_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_method_a()
        return f"The result of the B2 collaborating with the ({result})"
    
def create_product(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    
    print(f"{product_b.useful_method_b()}")
    print(f"{product_b.another_useful_method_b(product_a)}")

    
if __name__ == "__main__":
    
    create_product(ConcreteFactory1())
    print("\n")
    create_product(ConcreteFactory2())