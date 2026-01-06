# replace space with _
# string = 'hello hello'
# new_string = ''
# for char in string:
#     if char == ' ':
#         new_string+='_'
#     else:
#         new_string+= char
# print(new_string)       





# remove all the vowels from string
# string = input('enter the string')
# new_string = ''
# for char in string:
#     if char not in 'AEIOUaeiou':
#          new_string+= char
# print(new_string)       



# revrs the string without slicing

# string = input('enter the string:')
# rev_string = ''
# for char in string:
#     rev_string = char + rev_string
#     print(rev_string)


# slicing
# string = 'hello'
# print(string[5::-1])


# wap to get the followin


# num = int(input("Enter a number: "))

# if num > 1:  # Prime numbers are greater than 1
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")





# ÷enumerate  take list of string get the string presnet in odd pos using enum

list_ =['apple','ball','cat','ssss']
for index, string in enumerate(list_):
    if index%2!=0:
        print(index,string)

# ovel n even pos
list_ =['apple','ball','cat','ssss','aaaa','A']
out=[ ]
for index, string in enumerate(list_):
    if index%2==0 and string[0] in 'AEIOUaeiou':
          out.append((index,string))

        #   print(index,string)
          







































# notes
          
## it helps to execute the instructions n number of time
## by default it starts from first element of the collection and move till the length

## syntax:

# for variable in collections:
#     TSB

## range(): it helps to create the sequence of numbers in the given limit
## syntax: range(start_value, end_value +/- 1, updation)
## it will always include the start_value and always excludes the end value
## the default value for start is 0 and default value for updation is 1
## the range() gets the integer values

## WAP to print number from 0 to 10

# for num in range(0, 10+1, 1):
#     print(num)

## WAP to print alternate number from 0 to 20

# for num in range(0, 21, 2):
#     print(num)

## WAP to print number from 10 to 0

# for num in range(10, 0-1, -1):
#     print(num)

## Take the string "Hello" get character and index position at same time using range()

# string = 'Hello'
# for index in range(len(string)):
#     print(index, string[index])

## WAP TO EXTRACT ALL THE DIGITS FROM THE GIVEN STRING

# string = input('enter the string: ')
# new_string = ''
# for char in string:
#     if char.isdigit():
#         new_string += char
# print(new_string)

##or

# string = input('enter the string: ')
# new_string = ''
# for index in range(len(string)):
#     if string[index].isdigit():
#         new_string += string[index]
# print(new_string)

## Note:

## we can use range() in all the programs, but it is enough to use the range() only when the
## question asking about the index position

## wap to replace all the space in the given string with underscore using for loop(without using attribute)
# string = 'hello good evening'
##output: 'hello_good_evening'

# new_string = ''
# for char in string:
#     if char == ' ':
#         new_string += '_'
#     else:
#         new_string += char
# print(new_string)

## wap to remove all the vowels from the given string

# string = input('enter the string: ')
# res = ''
# for char in string:
#     if char not in 'AEIOUaeiou':
#         res += char
# print(res)

## wap extract all the single value data item from the list
# only if the element at even index position

# list_ = eval(input('enter the list: '))
# new_list = []
# for index in range(len(list_)):
#     if type(list_[index]) in [int, float, complex, bool] and index % 2 == 0:
#         new_list.append(list_[index])
# print(new_list)

##or

# list_ = eval(input('enter the list: '))
# new_list = []
# for index in range(0, len(list_), 2):
#     if type(list_[index]) in [int, float, complex, bool]:
#         new_list.append(list_[index])
# print(new_list)

## wap to reverse the string without using slicing
# string = 'hello'
##output: 'olleh'

# reverse_string = ''
# for char in string:
#     reverse_string = char + reverse_string
# print(reverse_string)

## wap to get the following output
# string = 'aaaabbbbbbccd'
##out: 'a4b6c2d1'

# char_count = ''
# for char in string:
#     if char not in char_count:
#         char_count += char + str(string.count(char))
# print(char_count)

# '' + 'a' + '4' ==> 'a4'
# 'a4' + 'b' + '6' ==> 'a4b6'

## wap to get the following output
string = 'aaaabbbbbbccd'
## output: {'a':4 , 'b':6 , 'c':2 , 'd':1}

# char_count = {}
# for char in string:
#     if char not in char_count:
#         char_count[char] = 1
#     else:
#         char_count[char] += 1
# print(char_count)

##or

# char_count = {}
# for char in string:
#     char_count[char] = string.count(char)
# print(char_count)

## wap to get the following output:
# string = 'aBBcDd@@7665&&LlDSs'
##output: 'ABBCDD@@7665&&LLDSS'

# out = ''
# for char in string:
#     if char.islower():
#         out += char.upper()
#     else:
#         out += char
# print(out)

## wap to get the following output
string = 'aBBcDd@@7665&&LlDSs'
#output: 'AbbCdD@@7665&&lLdsS'

# out = ''
# for char in string:
#     if char.islower():
#         out += char.upper()
#     elif char.isupper():
#         out += char.lower()
#     else:
#         out += char
# print(out)

##or

# out = ''
# for char in string:
#     if char.isalpha():
#         out += char.swapcase()
#     else:
#         out += char
# print(out)


## wap to get the following output
# string = 'aBBcDd@@7665&&LlDSs'
#output: 'AbbCdD7665lLdsS'

# out = ''
# for char in string:
#     if char.isalpha():
#         out += char.swapcase()
#     elif char.isdigit():
#         out += char
# print(out)

## wap to get the following output
# string = 'hello good evening'
##output: {'hello':5 , 'good':4 , 'evening' : 7}

# word_length = {}
# for word in string.split():           ## ['hello', 'good', 'evening']
#     word_length[word] = len(word)
# print(word_length)

## wap to get the following output
# list_ = ['python.py', 'google.com', 'yahoo.in', 'file.txt' , 'file.csv']
##output:['py', 'com', 'in', 'txt' , 'csv']

# extension = []
# for string in list_:
#     res = string.split('.')          ## ['python','py'], ['google', 'com']
#     extension.append(res[1])
# print(extension)

## wap to count the number of occurance of the specified character in the given string without using the attribute
# string = 'occurance'
# character = 'c'
## out = 3

# count = 0
# for char in string:
#     if char == character:
#         count += 1
# print(count)

## wap to replace the old character with new character without using the attribute
# string = 'occurance'
# old_char = 'c'
# new_char = 'C'
## out = 'oCCuranCe'

# new_string = ''
# for char in string:
#     if char == old_char:
#         new_string += new_char
#     else:
#         new_string += char
# print(new_string)

## wap to extract a string starting with vowel character
# list_ = ['Apple' , 'Google' , 'amazon', 'instagram', 'gmail', 'Extract']
# out = []
# for string in list_:
#     if string[0] in 'AEIOUaeiou':
#         out.append(string)
# print(out)

## wap to get the following output
l = [1,2,3,'hello' , 'hii' , -5,-4]
##o:[1,2,3,5,4]

# out = []
# for element in l:
#     if type(element) == int:
#         if element > 0:
#             out.append(element)
#         else:
#             out.append(-element)
# print(out)

##or

# out = []
# for element in l:
#     if type(element) == int:
#         out.append(abs(element))     ## abs(): it is an inbuilt function, which converts the -ve number to +ve whereas +ve number remians the same
# print(out)

## wap to get the following output
# string = 'python java web selenium SQL manual C++ jscript'
##output: {'python':6 , 'java':4 , 'web':'bew', 'selenium': 8 , 'SQL':'LQS' , 'manual':6 , 'C++':'++c', 'jscript':'tpircsj'}

# out = {}
# for word in string.split():
#     if len(word) % 2 == 0:
#         out[word] = len(word)
#     else:
#         out[word] = word[::-1]
# print(out)

## wap to extract all the non default  values from a list.
# l = [1,2,3, 0, 0.0, 'hii', '']
# o = [1,2,3,'hii']

# non_default_values = []
# for element in l:
#     if bool(element) == True:
#         non_default_values.append(element)
# print(non_default_values)

# wap to extract all the lowercase characters in a string only if the ascii value is  even.

# string = input('enter the string: ')
# new_string = ''
# for char in string:
#     if char.islower() and ord(char) % 2 == 0:
#         new_string += char
# print(new_string)

# wap to get the following output.
# In='hello'
# Out={0:’h’,1:’e’,2:’l’,3:’l’,4:’e’}

# index_char = {}
# for index in range(len(In)):
#     index_char[index] = In[index]
# print(index_char)

## wap to get the following output
# string = 'hello good evening'
##output: {'hello':'olleh' , 'good':'doog' , 'evening' : 'gnineve'}

## wap to get the following output
# string = 'hello good evening'
##output: {'hello':'ho' , 'good':'gd' , 'evening' : 'eg'}

# Wap to extract all the string values present in list only if the string is palindrome.
# Wap to extract all the odd number present at even index from a list.














