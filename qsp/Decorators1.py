
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

def Check_Even_Odd(some_thing):
    print(some_thing)
    def Inner(num):
        if num % 2 == 0:
            return some_thing(num)
        else:
            return "the number is odd"
    return Inner

# @Check_Even_Odd
def Get_Number(number):
    return number
# print(Get_Number(325))

## create the standalone function which gets string as input and return the same as output
## create one more function which have the functionality to reverse the string
## decorate the standalone function

def Reverse_String(some_thing):
    print(some_thing)
    def wrapper(String):
        return some_thing(String)[::-1]
    return wrapper

# @Reverse_String
def Get_Str(string):
    return string
# print(Get_Str('hello'))

## create the standalone function which takes any number of args and returns the same
## create a function which have the functionality
# to get the total number of args passsed and also invoke it
## decorate the standalone function

def calculate_num_of_args(some_thing):
    print(some_thing)
    def wrapper(*args, **kwargs):
        print(f'The number of args passed are {len(args) + len(kwargs)} ')
        return (some_thing(*args, **kwargs))
    return wrapper

# @calculate_num_of_args
def Get_Args(*args, **kwargs):
    print(args)
    print(kwargs)
# Get_Args(1,2,3)
# Get_Args(a = 1, b = 2, c = 3)
# Get_Args(1,2,3,a = 1, b = 2, c = 3)

## create the standalone function which takes any number as args and returns the square of input
## create a function which have the functionality, to check the number less than 0 if so print
## "invalid input" else invoke the function
## decorate the standalone function

def Check_Number(some_thing):
    print(some_thing)
    def wrapper(num):
        if num < 0:
            return "invalid input"
        else:
            return some_thing(num)
    return wrapper

# @Check_Number
def Get_Square(number):
    return number ** 2
# print(Get_Square(2))

## create the standalone function which takes any number of args
# either positional or keyword
## create one more function which have the functionality to accept only positional arg
## decorate the standalone function

def Accept_only_Pos_args(some_thing):
    print(some_thing)
    def wrapper(*args):
        return some_thing(*args)
    return wrapper

# @Accept_only_Pos_args
def Get_Arguments(*args, **kwargs):
    print(args)
    print(kwargs)
# Get_Arguments(1,2,3)
# Get_Arguments(a = 1, b = 2, c = 3)
# Get_Arguments(1,2,3,a = 1, b = 2, c = 3)

## create the standalone function which gets string input and return the same
## create one more function which have the functionality to execute the output 3 times
## decorate the standalone function

def execute_3_times(some_thing):
    print(some_thing)
    def wrapper(String):
        for i in range(3):
            print(some_thing(String))
    return wrapper

# @execute_3_times
def Get_String_(string):
    return string
# (Get_String_('hello'))

## create the standalone function which gets string input and return the same
## create one more function which have the functionality to convert the string to uppercase
## decorate the standalone function

def Convert_to_Uppercase(some_thing):
    print(some_thing)
    def wrapper(String):
        return some_thing(String).upper()
    return wrapper

# @Convert_to_Uppercase
def Get_String1_(string):
    return string
# print(Get_String1_('helLO54#^%$%'))

## create the standalone function which takes two args(a and b) and divide those two get the result as output
## create one more function whci have the functionality to check the value for b if it is 0
## print message "invalid input" else get the divison output
## decorate the standalone function

def Check_b_value(some_thing):
    print(some_thing)
    def wrapper(a, b):
        if b == 0:
            return "invalid input"
        else:
            return some_thing(a, b)
    return wrapper

@Check_b_value
def Division(a, b):
    return a / b
# print(Division(11,5))
print(Division(11,0))


















