

## syntax:

# if condition1:
#     if condition2:
#         TSB2
#     else:
#         FSB2
# else:
#     FSB1

## wap to print the length of collection only if it having length greater than 5

# data = eval(input('enter the data: '))
# if type(data) in [str, list, tuple, set, dict]:
#     if len(data) > 5:
#         print('The length of the collection is', len(data))
#     else:
#         print('The length is not greater than 5')
# else:
#     print('The data is of Single value type')

## wap to check the given character is vowel or not

# char = input('enter the character: ')
# if char.isalpha():
#     if char in 'aeiouAEIOU':
#         print('the given character is vowel')
#     else:
#         print('the given character is not vowel')
# else:
#     print('The character is not alphabet')

## Wap to check the person eligible for indian citizenship
# (only if person is above or equal to 18 years and indian)

# age = int(input('enter the age: '))
# nationality = input('enter the nationality: ')
# if age >= 18:
#     if nationality.upper() == 'INDIAN':
#         print('the person eligible for indian citizenship')
#     else:
#         print('the person not eligible for indian citizenship')
# else:
#     print('The age of person should be greater than or equal to 18')

## Wap to check the number is positive/negative and even/odd

# number = int(input('enter the number: '))
# if number > 0:
#     if number % 2 == 0:
#         print('the number is positive even')
#     else:
#         print('the number is positive odd')
# elif number < 0:
#     if number % 2 == 0:
#         print('the number is negative even')
#     else:
#         print('the number is negative odd')
# else:
#     print('The number is 0')

## WAP to print the reverse of string only if the string having middle char and startswith vowel
## and endswith consonants

# string = input('enter the string: ')
# if len(string) % 2 != 0:
#     if string[0] in 'AEIOUaeiou':
#         if string[-1] not in 'AEIOUaeiou':
#             print(string[::-1])
#         else:
#             print('The string not ending with consonants')
#     else:
#         print('The string not starting with vowel')
# else:
#     print('The string not having middle character')

## wap to check the user can login to the instagram by entering valid username and password
# username = 'abc_123'
# password = '123_abc'













