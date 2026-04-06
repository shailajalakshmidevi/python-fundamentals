
## Functions are the set of instructions to perform of some task

## therea re 2 types
##1. inbuilt function: these are the functions which are already developed by developer. ex: len(), id(), range()
##2. user defined function: these are functions we are created by user based on our requirment

## syntax:

# def fname(args):
#     TSB
#     return values
# fname(value)

##1. def : it is keyword, which helps to define the function
##2. fname: it is used to identify the function
##3. args: these are required to perfrom some operation
    ## there are 2 types in args
        ##1. Formal args: these are the args which we pass in the function defination
        ##2. Acutal args: these are the args which we pass in the function call
            ## The number of acutal and formal args should be equal
##4. return: it is a keyword, which helps to make the control to come out of the function
##5. function call: it is mandatory to execute the created function

## Based on the args and return value the function classified into 4types

##1. Function without args without return value
##2. Function with args without return value
##3. Function without args with return value
##4. Function with args with return value

#################################################################################################

##1. Function without args without return value

##1. WAP TO EXTRACT ALL THE INTEGER FROM THE GIVEN LIST

# data = eval(input('enter the data: '))
# out = []
# for element in data:
#     if type(element) == int:
#         out.append(element)
# print(out)

##or

def ext_int():
    data = eval(input('enter the data: '))
    out = []
    for element in data:
        if type(element) == int:
            out.append(element)
    print(out)
# ext_int()

##2. WAP TO GET THE FOLLOWING OUTPUT
# string  = 'abcDEF'
# out = {'a':97, 'b':98, 'c':99 ....}

def char_ascii():
    string = input('enter the string: ')
    out = {}
    for char in string:
        out[char] = ord(char)
    print(out)
# char_ascii()

##################################################################################################

##2. Function with args without return value

##1. WAPT CHECK THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS OR NOT

# string = input('enter the string: ')
# lower_count = 0
# for char in string:
#     if char.islower():
#         lower_count += 1
# if lower_count == 2:
#     print('THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS')
# else:
#     print('THE STRING NOT HAVING EXACTLY 2 LOWERCASE CHARACTERS')

#or

def count_lowercase(string):
    lower_count = 0
    for char in string:
        if char.islower():
            lower_count += 1
    if lower_count == 2:
        print('THE STRING HAVING EXACTLY 2 LOWERCASE CHARACTERS')
    else:
        print('THE STRING NOT HAVING EXACTLY 2 LOWERCASE CHARACTERS')
# count_lowercase('heLO')

## WAP TO EXTRACT ALL THE COMPLEX NUMBER FROM THE SET COLLECTION ,
# ONLY IF THE REAL PART OF THE COMPLEX NUMBER IS GREATER THAN 10
# ## set_ = {34, 5.6, -9-9j, 45 + 6j, 3 + 79j, 'hello', 11 - 9j}
# out = {45 + 6j, 11 - 9j}

def ext_complex(set_):
    out = set()
    for element in set_:
        if type(element) == complex and element.real > 10:
            out.add(element)
    print(out)
# ext_complex({34, 5.6, -9-9j, 45 + 6j, 3 + 79j, 'hello', 11 - 9j})

###################################################################################

##3. Function without args with return value

##1. WAP TO EXTRACT ALL THE KEY VALUE PAIR FROM THE DICTIONAY
# ONLY IF THE  VALUE IS INTEGER TYPE AND IT SHOULD BE GREATER THAN 10

def create_dict():
    dict_ = eval(input('enter the dict: '))
    out = {}
    for key, value in dict_.items():
        if type(value) == int and value > 10:
            out[key] = value
    return out
# print(create_dict())

##2. WAP TO GET PRODUCT OF N NATURAL NUMBERS/ FACTORIAL OF N NATURAL NUMBERS

## 4 ==>  1 * 2 * 3 * 4 ==> 24

def Factorial():
    number = int(input('enter the number: '))
    product = 1
    for num in range(1, number+1):
        product *= num
    return product
# print(Factorial())

#############################################################################

##4. Function with args with return value

##1. WAP TO EXTRACT ALL THE KEY VALUE PAIR FROM THE DICTIONAY
# ONLY IF BOTH KEY AND VALUE ARE OF SAME TYPE

def Create_Dict(dict_):
    out = {}
    for key, value in dict_.items():
        if type(key) == type(value):
            out[key] = value
    return out
# print(Create_Dict({'a':'apple', 8:9, 90:7.8}))

##or

def Create_Dict_(dict_):
    out = {}
    for key in dict_:
        if type(key) == type(dict_[key]):
            out[key] = dict_[key]
    return out
# print(Create_Dict_({'a':'apple', 8:9, 90:7.8}))

## WAP TO EXTRACT ALL THE FLOAT VALUES FROM THE LIST

def ext_float(list_):
    out = []
    for element in list_:
        if type(element) == float:
            out.append(element)
    return out
# print(ext_float([1, 2.3, 5.6, 7.8, 'hii']))

################################################################################

## WAP TO FIND THE SUM OF ASCII VALUE OF ALL THE SPECIAL CHARACTER PRESENT IN THE STRING
## WAP TO GET THE FOLLOWING OUTPUT
# LIST_ = [12, 0.0, 'HELLO', [], 9-9j]
# OUT = [True, False, True, False, True]