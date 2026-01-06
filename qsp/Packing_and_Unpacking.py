
## Packing: it helps to group the individual data item in the form of collection

##1. Tuple Packing
##2. Dictionary Packing

##############################################################################################

##1. Tuple Packing: it helps to group the individual data item in the form of tuple
## we can pass 0 to n number of positional only args
## to collect the excess positional args we use "*args"

## syntax:

# def fname(*args):
#     TSB
# fname(v1, v2,......)

##1.

def Get_pos_args(*args):
    print(args)
# Get_pos_args()
# Get_pos_args(1,2,3,4,5,6,7, 'hiii', [7, 90])

## Create a function which takes n number of positional args and extract only integer number from it

def ext_int(*values):
    print(values)
    for value in values:
        if type(value) == int:
            print(value)
# ext_int()
# ext_int(2,3.5,4,5,6,7, 'hiii', [7, 90],{1,2})

## Create a function which takes n number of positional args and extract only even integer number from it

def Even_int(*values):
    print(values)
    for value in values:
        if type(value) == int and value % 2 == 0:
            print(value)
# Even_int(2,3.5,4,5,6,7, 'hiii', [7, 90],{1,2})

#####################################################################################

## Dictionary Packing: it helps to group the individual data item in the form of dict
## we can pass 0 to n number of keyword only args
## to collect these keyword args we use "**kwargs"

## syntax:

# def fname(**kwargs):
#     TSB
# fname(k1 = v1, k2 = v2.......)

##1.

def Get_Key_Args(**kwargs):
    print(kwargs)
# Get_Key_Args()
# Get_Key_Args(a = 1, b = 2, c = 3)

## Create the function which takes n number of keyword only args get only those key-value
## whose value belongs to string type

def Key_Value(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        if type(value) == str:
            print(key, value)
# Key_Value()
# Key_Value(a = 1, b = 2, c = 'hello')

############################################################################################

## Variable arguments: it helps to pass both positional and the keyword args

## syntax:

# def fname(*args, **kwargs):
#     TSB
# fname(v1, v2,.....)  ## or
# fname(k1 = v1, k2 = v2,...)  ## or
# fname(v1, v2,..k1 = v1, k2 = v2,...)

##1.

def Get_Pos_Key_arg(*args, **kwargs):
    print(args, kwargs)
# Get_Pos_Key_arg()
# Get_Pos_Key_arg(1,2,3,4)
# Get_Pos_Key_arg(a = 1, b = 2, c = 3)
# Get_Pos_Key_arg(1,2,3,4,a = 1, b = 2, c = 3)

## Create a function which takes both positional and keyword args
## get only float value from tuple
## get the key-value pair only if the value belong to int type and greater than 10

def Get_Pos_Key_Args(*args, **kwargs):
    print(args, kwargs)
    for value in args:
        if type(value) == float:
            print(value)

    for key, value in kwargs.items():
        if type(value) == int and value > 10:
            print(key, value)
# Get_Pos_Key_Args(1, 2.3, 4.5, 'hii')
# Get_Pos_Key_Args(a = 12, b = 2, c = 45)
# Get_Pos_Key_Args(1, 2.3, 4.5, 'hii',a = 12, b = 2, c = 45)

######################################################################################

## Unpacking: it helps to divide the collection into individual data item

## syntax:

# def fname(arg1, arg2,...):
#     TSB
# fname(*collections)

## unpacking the list

list_ = ['Qspiders', 99.7, (21, 8, 2025)]
institute, share, date_ = list_
print(institute, share, date_)

## unpacking the tuple

date, month,year = date_
print(date, month, year)

## when we try to unpack the collection the number of variables should always be equal to length of the collection

## unpacking the string

string = 'hai'
char1, char2, char3 = string
print(char1, char2, char3)

def Unpack(var1, var2, var3, var4, var5):
    print(var1, var2, var3, var4, var5)
Unpack(*'hello')
Unpack(*[1,2,3,4,5])
Unpack(*(11,22,33,44,55))
Unpack(*{1,2,3,4,5})
Unpack(*{'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
Unpack(*{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.values())
Unpack(*{'a':1, 'b':2, 'c':3, 'd':4, 'e':5}.items())

## when we use function to unpack the collection
## the number of variables we use in function defination should be equal to length of the collection we have in function call




