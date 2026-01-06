## now will create the generic class and make it as abstrct class

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def start(self):
        pass

    def info(self):          ## concrete method
        print('you are using vehicle class')

# v = Vehicle(1)
# print(v.capacity)
# v.start()

## inherit the class we want to make it as abstarct with the ABC class present in abc module
## to make any class as abstrct we must have abstrctmethod in it, it restrict us not to creta the object

