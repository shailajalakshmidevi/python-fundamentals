
## break: it is a keyword, ASA the control encounter the break keyword it comes out of the loop
## and never go back to the same loop

## WAP to guess the number game

# number = 10
#
# while True:
#     user_input = int(input('Guess the number: '))
#     if user_input == number:
#         print('Congrats, you won the game')
#         break
#     elif user_input > number:
#         print('sorry, you guessed the larger number try again!!')
#     else:
#         print('sorry, you guessed the smaller number try again!!')

##2. WAP TO CHECK THE GIVEN INTEGER NUMBER IS PRIME NUMBER OR NOT

# number = int(input('enter the number: '))
# if number <= 1:
#     print('The number is not prime')
# else:
#     for num in range(2, number):
#         if number % num == 0:
#             print('The number is composite')
#             break
#     else:
#         print('The number is prime')

## WAP TO CHECK THE GIVEN TUPLE IS HOMOGENOUS OR NOT

# tuple_ = eval(input('enter the tuple: '))
# for element in tuple_:
#     if type(tuple_[0]) != type(element):
#         print('The Given Tuple is Hetrogenous')
#         break
# else:
#     print('The given tuple is homogenous')

##WAP TO PRINT THE INITIAL INDEX OF THE GIVEN CHARATER
# STRING = 'INITIAL'
# CHAR = 'I'
# out: index - 0

# for index in range(len(STRING)):
#     if STRING[index] == CHAR:
#         print(index, STRING[index])
#         break

###########################################################################################

## continue: it is keyword, ASA the control encounter the  continue keyword it pause the current execution
## and go back to same loop for further instructions

#1. WAP TO GET THE FOLLOWING OUTPUT
# string = 'hello hiii how are youu'
# # out = ['olleh', 'woh', 'era']
# out = []
# for word in string.split():
#     if len(word) % 2 == 0:
#         continue
#     else:
#         out.append(word[::-1])
# print(out)

##2. WAP TO PRINT THE PALINDROME NUMBERS IN THA RANGE 10 TO 100

# for num in range(10, 101):
#     if str(num) != str(num)[::-1]:        ## '10' != '01', '11' != '11'
#         continue
#     else:
#         print(num)

##or

# for num in range(10, 101):
#     if num % 11 != 0:        ## '10' != '01', '11' != '11'
#         continue
#     else:
#         print(num)

##4. WAP TO EXTRACT ALL THE COMPLEX NUMBERS FROM THE GIVEN SET COLLECTION

# set_ = eval(input('enter the set: '))
# res = set()
# for element in set_:
#     if type(element) != complex:
#         continue
#     else:
#         res.add(element)
# print(res)

##4. Wap to extract all the charcter from the string execpt the uppercase vowel

# string = input('enter the string: ')
# out = ''
# for char in string:
#     if char in 'AEIOU':
#         continue
#     else:
#         out += char
# print(out)

######################################################################################

## pass: it is a keyword, it helps to make the empty statement block valid

for num in range(1, 10):
    pass

for num in range(1, 10):
    if num % 2 == 0:
        pass











