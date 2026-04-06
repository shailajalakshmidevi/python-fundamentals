
## Control Statement helps in controlling the flow of execution based on 2 types

##1. based on some decision/ condition
##2. when we want to execute same set of instructions "n" number times

## There are two types in Control Statement

##1. Conditional/Decisional Statement
##2. Looping Statement

#################################################################################

##1. Conditional/Decisional Statement: it helps in controlling the flow of execution based n some decision/ condition

## There are 4 types

##1. if_condition
##2. else condition
##3. elif condition
##4. nested if condition

########################################################################################

##1. if_condition: "if" is a keyword, it will execute the TSB only when the condition is satisified
## if condition is not satisified it will ignore

## syntax:

# if condition:
#     TSB

## wap to check the given integer number is greater than 15

# number = int(input('enter the number: '))
# if number > 15:
#     print('the given integer number is greater than 15')

## WAP TO CHECK THE GIVEN INTEGER NUMBER IS EVEN

# number = int(input('enter the number: '))
# if number % 2 == 0:
#     print('THE GIVEN INTEGER NUMBER IS EVEN')

## wap to check the string is having exactly 5 characters

# string = input('enter the string: ')
# if len(string) == 5:
#     print('the string is having exactly 5 characters')

## wap to check the given data is integer

# data = eval(input('enter the data: '))
# if type(data) == int:
#     print('the given data is integer')

## wap to check the given character is uppercase

# char = input('enter the character: ')
# if char.isupper():
#     print('the given character is uppercase')

## wap to check the given string is having even number of charcater

# string = input('enter the string: ')
# if len(string) % 2 == 0:
#     print('the given string is having even number of charcater')

## wap to check the given string starts with vowel character

# string = input('enter the string: ')
# if string[0] in 'aeiouAEIOU':
#     print('the given string starts with vowel character')

##or

# string = input('enter the string: ')
# if string.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')):
#     print('the given string starts with vowel character')

## wap to check the given number is divisible by 3 and multiple of 5

# number = int(input('enter the number: '))
# if number % 3 == 0 and number % 5 == 0:
#     print('the given number is divisible by 3 and multiple of 5')

## wap to check the given data is single value datatype

# data = eval(input('enter the data: '))
# if type(data) == int or type(data) == float or type(data) == complex or type(data) == bool:
#     print('the given data is single value datatype')

##or

# data = eval(input('enter the data: '))
# if type(data) in [int, float, complex, bool]:
#     print('the given data is single value datatype')

## wap to check the given character is a lowercase
## wap to check the given character is a digit
## wap to check the given string having odd number of charcater
## wap to check the given integer number is positive
## wap to check the given data is string
## wap to check the given data is dictionary

