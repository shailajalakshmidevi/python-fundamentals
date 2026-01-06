
a = 10
# print(type(a))            ## a is one of the objects of int classs

l = [1,2,3]
# print(type(l))            ## l is one of the obejcts of list class

def Sam():
    pass
# print(Sam)
# print(type(Sam))          ## Sam is one of the objects of function class

#####################################################################################

## class: it is a blueprint which consists of properties and functionalities

## syntax:

# class cname:
#     properties/functionalities

## object: it is the instance of class, for a single class we can have n number of objects

## syntax: obj = cname()

#######################################################################################

## Type of states/ properties:

## There are 2 types of properties/states we can have inside the class

##1. class/Generic member: These are the members of class which are common for all the obejcts
##2. object/sepcific member:These are the members of object which are differnt for differnt object

## example:

# class             : company
# object            : Employees
# class member      : CEO, Location, rules and regulations, working hours
# object member     : Salary, Id, ph_no, Laptop, name, mail_id

#####################################################################################################

class Point:        ## Point is a class name
    a = 10         ## a and b are the class members
    b = 20

P1 = Point()       ## P1 and P2 are the objects
P2 = Point()

## syntax to access the class member => classname.classmember
## syntax to access the object member => objectname.objectmember

print(Point.a, Point.b)
print(P1.a, P1.b)
print(P2.a, P2.b)
## we can access the class members using the object
print(dir(Point))
print(dir(P1))
print(dir(P2))
print(Point.__dict__)     ## when we use __dict__ on the class name it will return all the classs members in the form of dict
print(P1.__dict__)        ## when we use __dict__ on object it will retun all the obect members in the form of dict

## syntax to modify the class member => classname.classmember = new_value
## syntax to modify the object member => objectname.objectmember = new_value

Point.a = 1000
P1.b = 2000

print(Point.a, Point.b)
print(P1.a, P1.b)
print(P2.a, P2.b)

## when we try to modify anything wrt class it will modify in all the obejcts
## when we try to modify anything wrt object it will modify only wrt to particular object

#####################################################################################

## init method/ constructor method/ initialization method

## it used to initialize the object members for the obejct
## it always takes "self" as first arg, which is responsible to get the address of object for which we need to create the object member
## no need of invoking the method outside the class, it will get invoked when we create the obejct for that class

## syntax:

# class cname:
#     classmember
#
#     def __init__(self, args1, arg2,........):
#         self.arg1 = arg1
#         self.arg2 = arg2
#
# ob1 = cname(val1, val2........)


class School:
    S_name = 'abc_school'
    S_loc = 'bangalore'

    def __init__(self, s_name, s_age, s_id):
        self.s_name = s_name
        self.s_age = s_age
        self.s_id = s_id

s1 = School('abc', 12, 123)
s2 = School('xyz', 13, 456)

print(School.S_name, School.S_loc)
print(s1.S_name, s1.S_loc, s1.s_name, s1.s_age, s1.s_id)
print(s2.S_name, s2.S_loc, s2.s_name, s2.s_age, s2.s_id)
print(School.__dict__)
print(s1.__dict__)
print(s2.__dict__)

print(dir(s1))
print(dir(s2))
print(dir(School))

## we can't access the object members using the class
## we can access the class members using the obejct




