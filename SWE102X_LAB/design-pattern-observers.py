from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List

class Subject(ABC):
    
    @abstractmethod
    def register(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def unregister(self, observer: Observer) -> None:
        pass
    
    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []
    
    def register(self, observer: Observer) -> None:
        self._observers.append(observer)
    
    def unregister(self, observer: Observer) -> None:
        self._observers.remove(observer)
    
    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
    
    def some_logic_business(self):
        self._state = randrange(0, 10)
        self.notify()
        pass
    
class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reached to the event")
            
    
class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reached to the event")
def client_code():
    pass

if __name__ == "__main__":
    subject = ConcreteSubject()
    
    obA = ConcreteObserverA()
    obB = ConcreteObserverB()
    subject.register(obA)
    subject.register(obB)
    subject.some_logic_business()

