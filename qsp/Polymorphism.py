
## it is the process of usning the same method/operators to work on differnt operation

## there are 3types

##1. Operator Overloading
##2. Method Overloading
##3. Method Overriding

######################################################################################

##1. Operator Overloading: All the operators works on builtin class but not on user defined class
## to make the operator work on user defined class we use operator overloading

class Sam:
    def __init__(self,a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __sub__(self, other):
        return self.a - other.a

    def __mul__(self, other):
        return self.a * other.a

s1 = Sam(1)
s2 = Sam(2)
# print(dir(Sam))
# print(s1.__add__(s2))
# print(s2.__sub__(s1))
# print(s1.__mul__(s2))

#############################################################################################

## Method Overloading: Python doesn't support method overloading by default
## here we will have same method name with different number of args inside the same class

class Demo1:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

D1 = Demo1()
# print(D1.add(1,2))
# print(D1.add(1,2,3))

## using default value

class Demo2:
    def add(self, a, b, c = 0):
        return a + b + c

D2 = Demo2()
# print(D2.add(1,2,3))
# print(D2.add(1,2))


## using *args

class Demo3:
    def add(self, *args):
        print(args)
        total = 0
        for num in args:
            total += num
        return total

D3 = Demo3()
print(D3.add())
print(D3.add(1,2,3,4,5,6,7,8,9))

###########################################################################################

## Method Overriding: we must have atleast 2 class, here we will have same method name
## same number of args but the functionality differs based on the location where it is present

class Bank1:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def add_method(self):
        print('we are using Bank1 class')

b1 = Bank1('abc', 20000)
print(b1.name, b1.balance)
b1.add_method()

class Bank2(Bank1):

    def add_method(self):
        print('we are using Bank2 class')

b2 = Bank2('xyz', 30000)
print(b2.name, b2.balance)
b2.add_method()




















