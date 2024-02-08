#------------- Design Pattern 1 -----------------
import time
from typing import Any

#--Closures
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# full_name = outer_function("Manish")
# print(full_name(" Rai"))


# Decorator in Python

def log_calls(func):
    def wrapper(*args,**kwargs):
        now = time.time()
        print("Calling {0} with {1} and {2}.".format(func.__name__,args,kwargs))
        return_value = func(*args,**kwargs)
        print("Executed {0} with {1}".format(func.__name__,time.time()-now))
        return return_value
    return wrapper

def test1(a,b,c):
    print("\tCalled test1.")

def test2(a,b):
    print("\tCalled test2.")

def test3(a,b):
    print("\tCalled test3.")
    time.sleep(1)

# test1 = log_calls(test1)
# test2 = log_calls(test2)
# test3 = log_calls(test3)

# test1(7,5,9)
# test2(5,b=1)
# test3(a=4,b=6)
    
# --------------- The observer pattern ---------------
class Inventory:
    def __init__(self):
        self.observers = []
        self._quantity = 0
        self._product = None

    def attach(self,observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self,value):
        self._product = value
        self._update_observer()

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self,value):
        self._quantity = value
        self._update_observer()

    def _update_observer(self):
        for observer in self.observers:
            observer()

class ConsoleObserver:
    def __init__(self,inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

# i = Inventory()
# c = ConsoleObserver(i)
# i.attach(c)
# i.product = "Widget"
# i.quantity = 10