
## while loop helps in executiong the insyrctions n number of times
## it will execute tillll the condition become False

## syntax:

# initialization
# while condition:
#     TSB
#     updation

# i = 1
# while i <= 3:
#     print('hello')
#     i += 1

## WAP TO PRINT N NATURAL NUMBERS

# number = int(input('enter the number: '))
# i = 1
# while i <= number:
#     print(i)
#     i += 1

## Print multiplication table of a number

# 2 X 1 = 2
# 2 X 2 = 4
#
# 2 X 10 = 20

# number = int(input('enter the number: '))
# i = 1
# while i <= 10:
#     print(f'{number} X {i} = {number * i}')
#     i += 1

## WAP TO PRINT "N NATURAL" NUMBERS WHICH ARE DIVISIBLE BY 3

# number = int(input('enter the number: '))
# i = 1
# while i <= number:
#     if i % 3 == 0:
#         print(i)
#     i += 1

##or

# number = int(input('enter the number: '))
# i = 3
# while i <= number:
#     if i % 3 == 0:
#         print(i)
#     i += 3

## Countdown from N to 1

# number = int(input('enter the number: '))
# while number > 0:
#     print(number)
#     number -= 1

## WAP TO EXTRACT ALL THE LOWERCASE CHARACTER FROM THE GIVEN STRING

# string = input('enter the string: ')
# new_string = ''
# i = 0
# while i < len(string):
#     if string[i].islower():
#         new_string += string[i]
#     i += 1
# print(new_string)


# '' + 'a' ==> 'a'
# 'a' + 'c' ==> 'ac'

## WAP TO EXTRACT ONLY THE INTEGER FROM THE LIST COLLECTION

# list_ = eval(input('enter the list: '))
# new_list = []
# i = 0
# while i < len(list_):
#     if type(list_[i]) == int:
#         new_list += [list_[i]]
#     i += 1
# print(new_list)

# [] + [1] ==> [1]
# [1] + [4] ==> [1,4]

##or

# list_ = eval(input('enter the list: '))
# new_list = []
# i = 0
# while i < len(list_):
#     if type(list_[i]) == int:
#         new_list.append(list_[i])
#     i += 1
# print(new_list)

## WAP TO REMOVE THE DUPLICATE VALUES FROM THE LIST WITHOUT TYPECASTING
NAMES = ['apple', 'google', 'apple', 'apple', 'insta']
# out = ['apple', 'google', 'insta']

# print(list(set(NAMES)))       ## with typecasting

# unique_elements = []
# i = 0
# while i < len(NAMES):
#     if NAMES[i] not in unique_elements:
#         unique_elements.append(NAMES[i])
#     i += 1
# print(unique_elements)

## WAP TO EXTRACT ALL THE FLOAT FROM THE TUPLE COLLECTION

# tuple_ =  eval(input('enter the tuple: '))
# new_tuple = ()
# i = 0
# while i < len(tuple_):
#     if type(tuple_[i]) == float:
#         new_tuple += (tuple_[i],)
#     i += 1
# print(new_tuple)

## WAP TO EXTRACT ALL THE INT NUMBERS FROM THE TUPLE ONLY IF THE NUMBER
# PRESENT AT ODD INDEX POSITION

# tuple_ = eval(input('enter the tuple: '))
# new_tuple = ()
# i = 0
# while i < len(tuple_):
#     if type(tuple_[i]) == int and i % 2 != 0:
#         new_tuple += (tuple_[i],)
#     i += 1
# print(new_tuple)

##or

# tuple_ = eval(input('enter the tuple: '))
# new_tuple = ()
# i = 1
# while i < len(tuple_):
#     if type(tuple_[i]) == int:
#         new_tuple += (tuple_[i],)
#     i += 2
# print(new_tuple)

## WAP TO CHECK THE GIVEN STRING IS PALINDROME OR NOT(without slicing)

# 'hello' ==> 'olleh'  ===> not palindrome
# 'noon' ==> 'noon' ===>  palindrome

# string = input('enter the string: ')
# reverse_string = ''
# i = 0
# while i < len(string):
#     reverse_string = string[i] + reverse_string
#     i += 1
# if string == reverse_string:
#     print('THE GIVEN STRING IS PALINDROME')
# else:
#     print('THE GIVEN STRING IS NOT PALINDROME')

## hai
# 'h' + '' ==> 'h'
# 'a' + 'h' ==> 'ah'
# 'i' + 'ah' ==> 'iah'

##hi
# 'h' + '' ==> 'h'
# 'i' + 'h' ==> 'ih'

## WAP to separate the positive and negative integer number present in list
l = [1,2,3,-5,-6,-7]
## positive = [1,2,3]    negative = [-5, -6, -7]

# positive = []
# negative = []
# i = 0
# while i < len(l):
#     if l[i] > 0:
#         positive.append(l[i])
#     else:
#         negative.append(l[i])
#     i += 1
# print(positive, negative)

## TAKE A STRING INPUT, EXTRACT ALL THE UPPERCASE, LOWERCASE, DIGITS AND SPECIAL CHARACTER IN 4 DIFFERENT VARIABLE
## WAP to Print All Divisors of a Number




















