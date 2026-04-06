
## Input Statement: it helps to get the input from the user

## syntax: var = input('msg')           ## msg is optional
## by default all the inputs will be stored in the form of string

## to have SVD as the input we use the following syntax

# var = int(input('msg'))
# var = float(input('msg'))
# var = complex(input('msg'))
# var = bool(input('msg'))


## to store MVD as input we use the following syntax

# var = eval(input('msg'))

## eval() we use in two case
##1. it helps to store the colletion value as input
##2. we can use it when we are not sure about the type values to be taken as input

## note:
##1. when we use eval() to store the string we must have the string inside the quotes else we get the error
## if the question already specify to take the string input it is enough to use input()
## and no need to have the string inside the quotes

###################################################################################

## Output Statement: print helps to get the output

a = 1
b = 2
# print(a, b)
# print(a, b, sep = '*************')
# print(a, b , sep = '**', end = '\ncompleted my task')

########################################################################################

## WAP to get the product of 2 integer number

# num1 = int(input('enter the number1: '))
# num2 = int(input('enter the number2: '))
# print(f'The product of {num1} and {num2} is', num2 * num1)
# print(num2 * num1)


## WAP TO GET THE LENGTH OF THE COLLECTION

data = eval(input('enter the data: '))
print(f'The length of given data {data} is', len(data))

## WAP TO GET THE REVERSE STRING

# string = input('enter the string: ')
# print(f'The reverse string of {string} is', string[::-1])

## WAP TO GET THE AREA OF TRIANGLE (0.5 * Base * Height)

# Base = eval(input('enter the base value: '))
# Height = eval(input('enter the height value: '))
# print('the area of triangle is', 0.5 * Base * Height)

## WAP TO GET THE LAST DIGIT OF GIVEN INTEGER INPUT

# number = int(input('enter the number: '))
# print(f'The last of given number {number} is', number % 10)

##or

# print(f'The last of given number {number} is',int(str(number)[-1]))

## 1234 ==> str(1234) ==> '1234' ===> '1234'[-1] ===> '4' ==> int('4') ==> 4





