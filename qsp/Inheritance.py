
## It is the process of derving the propeties from one class to another class
## The properties from which we inherit is called as Parent/ base / super class
## The properties to which we inherit is called as child / derived / sub class
## when we inherit the parent class to child it will inherit all the properties
## if we don't want the same in child class, we can redefine in child class

## There are 5 types

##1. Single level inheritance
##2. Multi level inheritance
##3. Multiple Inheritance
##4. Heirarchical Inheritance
##5. Hybrid Inheritance

#######################################################################################

## constructor chaining: it helps in invoking the construtor of parent class into the child class

## syntax

##1. super().__init__(args)
##2. parentname.__init__(self, args)

class School:
    def __init__(self, name, age, ph_no):
        self.name = name
        self.age = age
        self.ph_no = ph_no

s1 = School('anc', 12, 8765434567)
# print(s1.name, s1.age, s1.ph_no)

class New_School(School):
    def __init__(self, name, age, ph_no, Class, Section):
        super().__init__(name, age, ph_no)
        self.Class = Class
        self.Section = Section

s2 = New_School('abc', 14, 8765434567, 10, 'A')
# print(s2.name, s2.age, s2.ph_no, s2.Class, s2.Section)

################################################################################

##1. Single level inheritance: it is the process of inheriting the properties from single parent to single child class

## syntax:

# class Parent_Class:
#     TSB
#
# class Child_Class(Parent_Class):
#     TSB

class ShoppingCart:
    Product = {'iphone': 7, 'imac': 4, 'iwatch':6, 'ipad': 9}
    Price = {'iphone': 7000, 'imac': 4000, 'iwatch':6000, 'ipad': 9000}

    def __init__(self):
        self.cart = []

    def add_items(self, name, quantity = 1):
        if name not in self.Product.keys():          ## ['iphone', 'imac', 'iwatch', 'ipad']
            raise Exception('Product not available')
        elif self.Product[name] >= quantity:
            self.cart.append({'name': name, 'Price': self.Price[name], 'quantity': quantity})
        else:
            raise Exception('product out of stock')

    def Remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] == 1:
                    self.cart.remove(item)
                else:
                    item['quantity'] -= 1

S1 = ShoppingCart()
# print(S1.cart)
# S1.add_items('realme')
# S1.add_items('ipad')
# print(S1.cart)
# S1.add_items('iphone', 3)
# S1.add_items('iwatch', 4)
# S1.add_items('imac', 2)
# print(S1.cart)
# # S1.add_items('iphone', 40)
# S1.Remove_item('ipad')
# print(S1.cart)
# S1.Remove_item('iphone')
# print(S1.cart)

## create a class inherit it witj Shopping cart
## have the method to calculate total bill

class Calculate_Bill(ShoppingCart):
    def Toatl_Bill(self):
        return sum([item['Price'] * item['quantity'] for item in self.cart])

T1 = Calculate_Bill()
# print(T1.cart)
# T1.add_items('iphone', 4)
# T1.add_items('iwatch' ,3)
# T1.add_items('imac', 4)
# T1.add_items('ipad')
# print(T1.cart)
# print(T1.Toatl_Bill())

###########################################################################################

##2. Multi Level Inheritance: It is the process of derving the properties from one class to another class by considering more than one level

## syntax:

# class Class1:
#     TSB
#
# class Class2(Class1):
#     TSB
#
# class Class3(Class2):
#     TSB

##########################################################################################

##3. Multiple inheritance: It is process of derving child classs with multiple parent class


## syntax:

# class Parent_Class1:
#     TSB
#
# class Parent_Class2:
#     TSB
#
# class Parent_class3:
#     TSB
#
# class child_class(Parent_Class1, Parent_Class2, Parent_class3):
#     TSB


########################################################################################

##4. Heirarchical Inheritance: It is the process of derving the properties from single parent to multiple child class

## syntax:

# class Parent_Class:
#     TSB
#
# class child_class1(Parent_Class):
#     TSB
#
# class child_class2(Parent_Class):
#     TSB

####################################################################################

##5. Hybrid Inheritance: It is the process of combaining more than one type of inheritance















