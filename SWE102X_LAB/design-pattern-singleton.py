from typing import Any


class SingletonMeta(type):
    
    _instances = {}
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    def any_method(self):
        print("..helo")
        

if __name__ == "__main__":
    a = Singleton()
    b = Singleton()
    
    if a == b:
        print("OK")
    else:
        print("NOT OK")
    