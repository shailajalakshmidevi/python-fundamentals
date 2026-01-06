
## it is the process of hiding the implementaion and display the functionalities
## python doesn't support abstraction by default, to make any class as abstrct we need to import the module called abc

# class Bike:
#     def start(self):
#         print('starts with kick')
#
# class Scooty:
#     def start(self):
#         print('self start')
#
# class Car:
#     def start(self):
#         print('starts with key')

from Vehicle_Abstrction import Vehicle

class Bike(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('starts with kick')


class Scooty(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('self starts')


class Car(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('starts with key')

## when we inherit the abstrct class to child it is mandatory to have the abstrct method in it else it throws the error








