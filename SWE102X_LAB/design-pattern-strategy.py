from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Context():
    
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    
    def do_some_business_logic(self, data:List) -> None:
        result = self._strategy.do_algorithm(data)
        return result

class Strategy(ABC):
    
    @abstractmethod
    def do_algorithm(self, data:List) -> list:
        pass
    
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> list:
        return sorted(data)
    

class ConcreteStrategyB(Strategy):
    
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))

def client_code() -> None:
    context = Context(ConcreteStrategyA())
    
    data = ["a", "c", "b", "m", "e"]
    print(context.do_some_business_logic(data))
    
    context.strategy = ConcreteStrategyB()
    result = context.do_some_business_logic(data)
    print(f"result: {result}")
    print(f"type(result): {type(result)}")
    print(f"join: {','.join(result)}")
    pass

if __name__ == "__main__":
    client_code()
    