from __future__ import annotations

class Component():
    
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    
    _component: Component = None
    
    def __init__(self, component: Component):
        self ._component = component
    
    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self) -> str:
        return self._component.operation()
    
class ConcreteDecorator1(Decorator):
    
    def operation(self) -> str:
        return f"ConcreteDecorator1({self.component.operation()})"

class ConcreteDecorator2(Decorator):
    
    def operation(self) -> str:
        return f"ConcreteDecorator2({self.component.operation()})"

def client_code(component: Component):
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":
    simple = ConcreteComponent()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")
    
    decorator1 = ConcreteDecorator1(simple)
    decorator2 = ConcreteDecorator2(decorator1)
    
    client_code(decorator2)
    