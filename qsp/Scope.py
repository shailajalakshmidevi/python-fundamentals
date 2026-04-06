
def ext_str():
    list_ = eval(input('enter the list: '))
    out = []
    for ele in list_:
        if type(ele) == str:
            out.append(ele)
    return out
# print(list_)
# print(ext_str())
# print(list_)


# list_ = eval(input('enter the list: '))
# def ext_str_():
#     out = []
#     for ele in list_:
#         if type(ele) == str:
#             out.append(ele)
#     return out
# print(list_)
# print(ext_str_())
# print(list_)

###################################################################################

## Scope of variables: the variable we create works based on the location where it is present

## There are 2 types

##1. Global Variable
##2. Local Variable

###################################################################################

##1. Global Variable: These are variables which we create outside the function
## we can access both inside and outside the function

##1.

# a = 10
# b = 20                ## here a and b are the global variables
# def Sam():
#     return a + b
# print(Sam())

##2.

# a = 100
# b = 200                ## here a and b are global variables
# def Sam():
#     print(a + b)
#     print(b - a)
# print(b, a)
# Sam()
# a = 300
# print(a > b)

##########################################################################################

##2. Local Variables: these are the variables which we create inside the function
## we can access it only inside the function not outside

##1.

# a = 100
# b = 200                    ## here a and b are the global variable
# def Demo():
#     b = 300                ## b is local variable
#     return a + b
# print(Demo())

## Here it consider 300 for b variable because the control given first prefernce to local variable
## it moves to global scope only when there is no local variable

##2.

# a = 10
# b = 20
# def outer():
#     print(a + b)
#     print(a < b)
#     def inner():
#         m, n = 30, 40
#         print(n, m)
# print(b > a)
# outer()

##3.

# a = 10
# b = 20                 ## here a and b are the global variable
# def outer():
#     print(a + b)
#     print(a < b)
#     def inner():
#         m, n = 30, 40       ## here m and n are local variable for inner()
#         print(n, m)
#     print(a)
#     inner()
#     print(b)
# print(b > a)
# outer()

##4

# x = 10                       ## here x is global variable
# def outer():
#     x = 20                   ## here x is local variable for outer() and nonlocal variable for inner()
#     print(x)
#     def inner():
#         x = 30               ## here x is local variable for inner()
#         print(x)
#     print(x)
#     inner()
# outer()
# print(x)

##5

# a, b = 11,12
# def Demo():
#     a = a + 1
#     b = b + 1
#     return a + b
# print(Demo())

##6.

# a = 100
# def Sam():
#     global a            ## global keyword helps access and modify the global variable inside the function
#     a = a + 100
#     return a
# print(a)
# print(Sam())
# print(a)

##7.

# x = 10
# def outer():
#     x = 20
#     print(x)
#     def inner():
#         global x
#         x = x + 100
#         print(x)
#     print(x)
#     inner()
#     print(x)
# print(x)
# outer()
# print(x)

##8

# x = 10
# def outer():
#     x = 20
#     print(x)
#     def inner():
#         nonlocal x      ## nonlocal keyword helps to access and modify the nonlocal variable inside the nested function
#         x = x + 100
#         print(x)
#     print(x)
#     inner()
#     print(x)
# print(x)
# outer()
# print(x)

############################################################################################

## Function by passing the default values

## wkt to execute the function the number of actual and formal args should be equal if not will get the error
## but if we want to change the number of actual and formal args we can use default values
## in this case will pass all the mandatory args(positional args) first and then the non-mandatory args(keyword args)

## syntax:

# def fname(var1, var2,...... variable1 = defualt1, variable2 = default2,....):
#     TSB
# fname(val1, val2......)

##1.

# def Greet(name):
#     ## name is a mandatory arg
#     print(f'Hello {name}')
# Greet('Anu')

##2.

# def Greet(name = 'Anu'):
#     ## name is a non-mandatory arg
#     print(f'Hello {name}')
# Greet()

##3.

# def Greet(name = 'Anu'):
#     ## name is a non-mandatory arg
#     print(f'Hello {name}')
# Greet('Abhi')

## the first preference will be given to the value we pass in the function call for non-mandatory args
## the control takes the default value only when we don't pass the value in function call

##4

# def Greeting(name, age, pay):
#     ## here name, pay and age are the mandatory args
#     print(f'Hello myself {name} of age {age} years with pay Rs{pay}')
# Greeting('Sonu', 26, 20000)

##5.

def Greeting(name, age = 28, pay = 40000):
    ## here name, pay and age are the mandatory args
    print(f'Hello myself {name} of age {age} years with pay Rs{pay}')
# Greeting('Sonu', 26, 20000)
# Greeting('Sonu')
# Greeting(name = 'Sonu', age = 27, pay = 50000)
# # Greeting(name = 'Sonu',  27, pay = 50000)       ## it throws the error because we have passsed the positional arg after keyword
# Greeting('Sonu', 27, pay = 50000)

##6.

def Sam(name, debug = False):
    if debug:
        print('You are using Sam function')
    else:
        print(name[::-1])
# Sam('Monu')
# Sam('Monu', True)
# Sam(name = 'Monu', debug = True)
# Sam('Monu', debug = True)