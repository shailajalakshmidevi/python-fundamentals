
## else is a keyword, it will execute the TSB when the "if condition" is satisfied
## when if condition not satisfied it will execute FSB
## for single condition we will 2 SB

## syntax:

# if condition:
#     TSB
# else:
#     FSB

## wap to check the given number is odd or even

# number = int(input('enter the number: '))
# if number % 2 != 0:
#     print('the given number is odd')
# else:
#     print('the given number is even')

## wap to check the given string having a middle character or not

# string = input('enter the string: ')
# if len(string) % 2 != 0:
#     print('the given string having a middle character')
# else:
#     print('the given string not having a middle character')

## wap to check the two variables having integer values are pointing to same address or not

# num1 = int(input('enter the number1: '))
# num2 = int(input('enter the number2: '))
# if id(num1) == id(num2):
#     print('the two variables having integer values are pointing to same address')
# else:
#     print('the two variables having integer values are not pointing to same address')

##or

# num1 = int(input('enter the number1: '))
# num2 = int(input('enter the number2: '))
# if num1 is num2:
#     print('the two variables having integer values are pointing to same address')
# else:
#     print('the two variables having integer values are not pointing to same address')

## wap to check the first element of list is string or not

# list_ = eval(input('enter the list: '))
# if type(list_[0]) == str:
#     print('the first element of list is string')
# else:
#     print('the first element of list is not string')

## wap to check the first charcater in the string is uppercase or not,
# if uppercase get the reversed string else get the string as is

# string = input('enter the string: ')
# if string[0].isupper():
#     print(string[::-1])
# else:
#     print(string)

##  wap to check the last digit of the integer number is divisible by 3 or not

# number = int(input('enter the number: '))
# if (number % 10) % 3 == 0:
#     print('the last digit of the integer number is divisible by 3')
# else:
#     print('the last digit of the integer number is not divisible by 3')

##or

# number = int(input('enter the number: '))
# if int(str(number)[-1]) % 3 == 0:
#     print('the last digit of the integer number is divisible by 3')
# else:
#     print('the last digit of the integer number is not divisible by 3')

## wap to check the square of the integer number is even or odd,
# if even print 'hii' else print 'hello'

# num = int(input('enter the number: '))
# if (num ** 2) % 2 == 0:
#     print('hii')
# else:
#     print('hello')

## wap to check two variables are pointing to different address or not

## wap to check the given data is collection type or not





