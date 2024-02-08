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
        