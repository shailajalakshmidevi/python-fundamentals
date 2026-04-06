

## it helps to check multiple conditions

## syntax:

# if condtion1:
#     TSB1
# elif condition2:
#     TSB2
# elif condition3:
#     TSB3
#
# else:
#     FSB               ## else is not mandatory

## wap to check the relationship between two integer number

# num1 = int(input('enter the number1: '))
# num2 = int(input('enter the number2: '))
# if num1 == num2:
#     print('Both numbers are equal')
# elif num1 > num2:
#     print('Num1 is greater')
# elif num1 < num2:
#     print('Num2 is greater')

##or

# num1 = int(input('enter the number1: '))
# num2 = int(input('enter the number2: '))
# if num1 == num2:
#     print('Both numbers are equal')
# elif num1 > num2:
#     print('Num1 is greater')
# else:
#     print('Num2 is greater')

## wap to check the given character is uppercase or lowercase or number or special charcter

# char = input('enter the character: ')
# if char.isupper():
#     print('the given character is uppercase')
# elif char.islower():
#     print('the given character is lowercase')
# elif char.isdigit():
#     print('the given character is digit')
# else:
#     print('the given character is special')

##or

# char = input('enter the character: ')
# if 'A' <= char <= 'Z':
#     print('the given character is uppercase')
# elif 'a' <= char <= 'z' :
#     print('the given character is lowercase')
# elif '0' <= char <= '9':
#     print('the given character is digit')
# else:
#     print('the given character is special')

## wap to check the integer number is having exactly single or
# double or triple digit or more than 3 digit

# number = int(input('enter the number: '))
# if len(str(number)) == 1:
#     print('the integer number is having exactly single digit')
# elif len(str(number)) == 2:
#     print('the integer number is having exactly double digit')
# elif len(str(number)) == 3:
#     print('the integer number is having exactly triple digit')
# else:
#     print('the integer number is having more than three digits')

## take a string input,
##1. if the string having exactly 5 character print the given input
##2. if the string having less than 5 character print reverse string
##3. if the string having more than 5 character print alternate characters

# string = input('enter the string: ')
# if len(string) == 5:
#     print(string)
# elif len(string) < 5:
#     print(string[::-1])
# else:
#     print(string[::2])

## take a integer input,
##1. if given number is divible by 3 print 'hii'
##2. if given number is divible by 5 print 'byee'
##3. if given number is divible by 3 and also 5 print 'hiibyee'
# num = int(input("Enter the number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("hiibyee")
# elif num % 3 == 0:
#     print("hii")
# elif num % 5 == 0:
#     print("byee")


## wap to check the greater among 3 integer number
# num1 = int(input("enter the string"))
# num2 = int(input("enter the string"))

# num3 = int(input("enter the string"))

# if num1>num2:
#     print("num1 is grt")
# elif num2>num3:
#     print("num2 is grt")
# if num3>num1:
#     print("num3 is grt")





## wap to check the given character is alphabet or number or special
# char = input('enter the character: ')
# if char.isalpha():
#      print('the given character is alphabet')
# elif char.isnumeric():
#      print('the given character is number')
# else:
#      print('the given character is special')


# ## else

## wap to check two variables are pointing to different address or not

# wap to check the given data is collection type or not
     # eval is used to treat the values in the form of integer itself instead of string 
# data = eval(input("Enter any data: "))

# if isinstance(data, (list, tuple, set, dict)):
#     print("It is a collection type")
# else:
#     print("It is NOT a collection type")
     
data = eval(input("Enter any data: "))

if type(data) in ((list, tuple, set, dict)):
    print("It is a collection type")
else:
    print("It is NOT a collection type")
    
