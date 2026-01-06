
a = 10
b = a
# print(b, a)
# print(id(a), id(b))

###############################################################################

# def Sam():
#     return ('hello hii')
# Sam()

# print(Sam)

# x = Sam
# print(x)
# x()

###############################################################################

def Demo(some_thing):
    print(some_thing)
# Demo(Sam)

###############################################################################
def Sam():
    return ('hello hii')


def greeting(name):
    return (f'Hello {name}')

def greet(name, wish):
    return (f'Hello {wish} myself {name}')


def dummy(some_thing):
    print(some_thing)
    return some_thing('abc', 'good evening')
# print(dummy(Sam))
# dummy(greeting)
# dummy(greet)

#####################################################################################

def Dummy(some_thing, *args):
    print(some_thing)
    print(args)
    return some_thing(*args)
# print(Dummy(Sam))
# print(Dummy(greeting ,'abc'))

#####################################################################################

def Dummy1(some_thing):
    print(some_thing)
    def Dummy2(*args, **kwargs):
        print(args, kwargs)
        return some_thing(*args, **kwargs)
    return Dummy2('abc', wish = 'good evening')
# print(Dummy1(greet))

#####################################################################################
## adding few seconds of delay

def add(a, b):
    return a + b

import time
def delay(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        time.sleep(6)
        return some_thing(*args, **kwargs)
    return wrapper(11,40)
# print(delay(add))

#####################################################################################

## calculate the total execution time

def sub(a, b):
    return a - b

def Total_Time(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        time.sleep(5)
        res = some_thing(*args, **kwargs)
        end_time = time.time()
        Total_time = end_time - start_time
        print(f'The total execution time is {Total_time}')
        return res
    return wrapper(7,3)
# print(Total_Time(sub))

#############################################################################################

## Decorators: it helps to add the extra functionality to the function without maodifing anything the code

def delay(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        time.sleep(6)
        return some_thing(*args, **kwargs)
    return wrapper

# @delay
def add(a, b):
    return a + b
# print(add(11,22))

##############################################################################

def Total_Time(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        time.sleep(5)
        res = some_thing(*args, **kwargs)
        end_time = time.time()
        Total_time = end_time - start_time
        print(f'The total execution time is {Total_time}')
        return res
    return wrapper

# @Total_Time
def sub(a, b):
    return a - b
# print(sub(44,3))

###################################################################################

## create the standalone function which takes integer input retuns the same output
## create extra function which add the functionality
## to convert the negative to positive and positive be the same
## decorate the standalone function

def Convert_Negative(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        res = some_thing(*args, **kwargs)
        return abs(res)
    return wrapper

# @Convert_Negative
def get_number(number):
    return number
# print(get_number(-1))

###################################################################################

## create the standalone function which gets string "Hello Hii" as input and return tha same as output
## create one more function which have the functionality to to replace "Hii" by "bye"
## decorate the standalone function

def replace_substring(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        return some_thing(*args, **kwargs).replace('hii', 'bye')
    return wrapper

# @replace_substring
def Get_String(string):
    return string
# print(Get_String('hello hii'))

## create the standalone function which takes integer input retuns the same output
## create extra function which add the functionality, get the number if it is even
# else get message 'the number is odd'
## decorate the standalone function

