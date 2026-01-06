
## Exception: It is an unauthorized error which stops the program execution
## Exception handling: It is used to handle the errors we get in the program
## we can't handle the syntax error
## There are 4blocks
## try            ## except                   ## else              ## finally
## try and except are the mandatory whereas else and finally are optional
## in try block we will have the problem statement
## in except block we will have the solution for the problem

#############################################################################

## Specific exception handling:

# list_ = ['gmail', 'insta', 'gmail', 'gmail', 'insta']
# word_count = {}
# for word in list_:
#     word_count[word] += 1
# print(word_count)

## handle the keyerror

list_ = ['gmail', 'insta', 'gmail', 'gmail', 'insta']
word_count = {}
for word in list_:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1
# print(word_count)


def division(a, b):
    return a / b
# print(division(40,0))

## handle the ZeroDivisionError

def Division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "can't divide from 0"
# print(Division(50,'8'))

## handle the ZeroDivisionError and TypeError

def Div(a, b):
    try:
        out = a / b
    except ZeroDivisionError:
        print("can't divide from 0")
    except TypeError:
        print("The value for a and b should not be collection type")
    ## else will execute only when there is no error in the try block
    else:
        print(out)
    ## it executes in each execution
    finally:
        print('got some output')
# Div(40,'0')


## handling IndexError

## create the function inside which have a try block, inside the try block take
## user list input and user index input
## if the index present return the value else handle the error

def Index_Error():
    try:
        list_ = eval(input('enter the list: '))
        index = int(input('enter the index value: '))
        print(f'The element at index position {index} is {list_[index]}')
    except IndexError:
        print('index out of range')
# Index_Error()

## Handling the IndexError and ValueError

def Handle_Error():
    try:
        list_ = eval(input('enter the list: '))
        index = int(input('enter the index value: '))
        print(f'The element at index position {index} is {list_[index]}')
    except IndexError:
        print('index out of range')
    except ValueError:
        print('The index value should be always int type')
# Handle_Error()

##############################################################################

## Generic Exception Handling

list_ = ['gmail', 'insta', 'gmail', 'gmail', 'insta']
word_count = {}
for word in list_:
    try:
        word_count[word] += 1
    except:
        word_count[word] = 1
print(word_count)

def Division(a, b):
    try:
        return a / b
    except:
        return "Error Handled"
# print(Division(50,0))

def Handle_Error():
    try:
        list_ = eval(input('enter the list: '))
        index = int(input('enter the index value: '))
        print(f'The element at index position {index} is {list_[index]}')
    except Exception:
        print('error handled')
# Handle_Error()

##############################################################################

## Custom Exception Handling: it helps to throw the error whenever we want in out program
## syntax:  raise Errorname('msg')            ## msg is optional

# list_ = eval(input('enter the list: '))
# for ele in list_:
#     if type(ele) == int:
#         print(ele)
#     else:
#         raise TypeError('encountered non-int type')

## take 2 collection check the length of it
## if both having same length print "both have same length" else raise error

# data1 = eval(input('enter the data1: '))
# data2 = eval(input('enter the data2: '))
# if len(data2) == len(data1):
#     print("both have same length")
# else:
#     raise ValueError

##. create a function which takes mail id as input
## check if the mail id endswith ".com" and  contains "@" in it or not
## if the condition satisfied print mail id else raise exception

##########################################################################################

## User defined Exception: it helps to create our own errorname

## synatx:

# class Errorname(Exception):
#     pass

class InsufficientFunds(Exception):
    pass

def withdraw(amount):
    if amount < 1000:
        print('withdrawn')
    else:
        raise InsufficientFunds
# withdraw(5000)

## create a function which takes 2 arsg like username and password
## if username == 'python_123' aand password == '123_py'
## print "logged in" else raise your exception

class Login_Error(Exception):
    pass

def Login(username, password):
    if username == 'python_123' and password == '123_py':
        print('logged in')
    else:
        raise Login_Error
# Login('python_123', '123_py')

## create a function which takes number of questions as input
## if number of questoions is less than or equal to 25 print " yes, i will do it" if not
## else raise your exception









