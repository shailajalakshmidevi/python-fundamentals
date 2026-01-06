
## it helps to avoid the access of attributes/ methods outside the class

## there are 3 types

##1. Public Access Specifiers
##2. Protected Access Specifiers
##3. Private Access Specifiers

############################################################################################

##1. Public Access Specifiers: here we can access the attributes and the method outside the class

class School:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f'Hello myself {self.name}')

# s = School('abc')
# print(s.name)
# s.display_info()

######################################################################################

##2. Protected Access Specifiers: to make any method/attribute as protected we will have "_" before that
## Protected Access Specifiers works same as Public Access Specifiers

class School:
    def __init__(self, name, roll_no):
        self.name = name
        self._roll_no = roll_no

    def _display_info(self):
        print(f'Hello myself {self.name} with roll_no {self._roll_no}')

# s = School('abc', 123)
# print(s.name, s._roll_no)
# s._display_info()

###################################################################################

##3. Private Access Specifiers

class School:
    def __init__(self, name, roll_no, age):
        self.name = name
        self._roll_no = roll_no
        self.__age = age

    def __display_info(self):
        print(f'Hello myself {self.name} with roll_no {self._roll_no} of age {self.__age}')

s = School('abc', 123, 13)
print(s.name, s._roll_no)
# print(s.__age)
# s.__display_info()


## name mangling

## syntax to access the private attribute: objectname._classname__privateattribute
## syntax to access the private method: objectname._classname__privatemethod()

# print(s._School__age)
# s._School__display_info()































