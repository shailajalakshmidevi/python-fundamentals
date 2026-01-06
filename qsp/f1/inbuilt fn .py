
## enumerate(): it is a inbuilt function which gives the numbering to each element in the collection

string = 'hello'
# for index in range(len(string)):
#     print(index, string[index])

##or

# for item in enumerate(string):
#     print(item)

##or

# for index, char in enumerate(string):
#     print(index, char)


## or

# for index, char in enumerate(string, start = 10000000000000000000000000):
#     print(index, char)

## TAKE LIST OF STRING, GET THE STRING PRESENT AT ODD POSITION USEING ENUMEARTE
list_ = ['apple', 'google', 'amazon', 'youtube', 'insta', 'yahoo']
out = []
for index, string in enumerate(list_):
    if index % 2 != 0:
        out.append((index, string))
# print(out)

## TAKE LIST OF STRING, GET THE STRING PRESENT AT EVEN POSITION
# AND STRING SHOULD START WITH VOWEL
list_ = ['apple', 'google', 'Amazon', 'youtube', 'insta', 'yahoo']
out = []
for index, string in enumerate(list_):
    if index % 2 == 0 and string[0] in 'aeiouAEIOU':
        out.append((index, string))
# print(out)

## WAP TO PRINT THE SUM OF ALL THE NUMBERS PRESENT AT ODD INDEX IF THE NUMBER IS EVEN

#########################################################################################

## zip(): it is an inbuilt function, which helps to itrate over the multiple collection at same time
## the disadvange of zip() is it stops at least length collection

list1 = [1,2,3]
list2 = [4,5,6]

# for item in zip(list1, list2):
#     print(item)

##or

# for num1, num2 in zip(list1, list2):
#     print(num1, num2)

list3 = [1,2,3]
tuple1 = (11,22,33)
string = 'hai'

# for num1, num2, char in zip(list3, tuple1, string):
#     print(num1, num2, char)

list4 = [1,2,3,4,5,6,7,8,9]
tuple2 = (11,22,33)
string = 'py'

# for num1, num2, char in zip(list4, tuple2, string):
#     print(num1, num2, char)

## WAP TO GET THE FOLLOWING OUTPUT
LIST1 = [1,2,3,4]
LIST2 = [5,6,7,8]
# OUT = [5,12,21,32]

out = []
for num1, num2 in zip(LIST1, LIST2):
    out.append(num1 * num2)
# print(out)

#. WAP TO CREATE THE DICTIONARY BY USING GIVEN LIST
list_ = ['youtube', 'gmail','YAHOO', 'email', 'facebook', 'whatsapp', 'instagram']
_list = [1,2,3,5]

out = {}
for string, number in zip(list_, _list):
    out[string] = number
# print(out)

#####################################################################################

## zip_longest()

list4 = [1,2,3,4,5,6,7,8,9]
tuple2 = (11,22,33)
string = 'py'

# from itertools import zip_longest
# for num1, num2, char in zip_longest(list4, tuple2, string):
#     print(num1, num2, char)

##or

# from itertools import zip_longest
# for num1, num2, char in zip_longest(list4, tuple2, string, fillvalue = 'no pair found'):
#     print(num1, num2, char)

##oe

# from itertools import zip_longest
# for num1, num2, char in zip_longest(list4, tuple2, string, fillvalue = 0):
#     print(num1, num2, char)

#. WAP TO CREATE THE DICTIONARY BY USING GIVEN LIST
list_ = ['youtube', 'gmail','YAHOO', 'email', 'facebook', 'whatsapp', 'instagram']
_list = [1,2,3,5]
out = {}
from itertools import zip_longest
for string, number in zip_longest(list_, _list):
    out[number] = string
# print(out)

####################################################################################

## defaultdict

string = 'aaabbbaa'     ## out = {'a': 5, 'b':3}

out = {}
for char in string:
    if char not in out:
        out[char] = 1
    else:
        out[char] += 1
print(out)

##or

out = {}
for char in string:
    out[char] = string.count(char)
print(out)

## using defaultdict
from collections import defaultdict
out = defaultdict(int)
for char in string:
    out[char] += 1
# print(out)

##. Counting occurrences of items which starts with consonants
items = ['apple', 'banana', 'banana', 'orange', 'grape', 'apple', 'apple', 'banana', 'orange']
# out = {'banana': 3, 'grape': 1}

out = defaultdict(int)
for item in items:
    if item[0] not in 'aeiouAEIOU':
        out[item] += 1
print(out)

## Storing indices of items using enumerate()
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# out = {'apple': (0, 2, 5), 'banana': (1, 4), 'orange': (3,)}

out = defaultdict(tuple)
for index, item in enumerate(items):
    out[item] += (index, )
# print(out)

##or

out = {}
for index, item in enumerate(items):
    if item not in out:
        out[item] = (index, )
    else:
        out[item] += (index,)
print(out)


## Categorizing numbers as even or odd
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# out = {'odd': {1, 3, 5, 7, 9}, 'even': {8, 2, 4, 6}}

out = defaultdict(set)
for number in numbers:
    if number % 2 == 0:
        out['even'].add(number)
    else:
        out['odd'].add(number)
# print(out)

## WAP TO GET THE FOLLOWING OUTPUT
list_ = ['mango fruit', 'carrot veg', 'grape fruit', 'apple fruit', 'raddish veg']
# out = {'fruit': ['mango', 'grape', 'apple'], 'veg': ['carrot', 'raddish']}

##########################################################################

## isinstance()

list_  = [1, 2, 5.6, 'hii']
for element in list_:
    if type(element) == int:
        print(element)

for element in list_:
    if isinstance(element, int):
        print(element)

print(type(1))
print(isinstance(1.5, int))