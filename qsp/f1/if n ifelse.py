#wap to check two variables having integer values are poiting to same adress or not
# num1 = int(input('enter the num1:'))
# num2 = int(input('enter the num2:'))
# # if(id(num1)==id(num2)):
# if num1 is num2:
#     print('same adress')
# else:
#     print('no')
# wap to check the first element of list is string or not
# list=eval(input('enter the list'))
# if type(list[0])==str:
#     print('yes')
# else:
#     print('no')
#  wap to get the 1st char in the string is uppercase or not
# if uppercase get the reverse string else get the string
# string = input('enter the string')
# if string[0].isupper():
#     print(string[::-1])
# else:
#     print(string)





#     #  wap to check the last digit of the integer number is divisible iby 3 or not
# num = int(input("Enter an integer: "))
# # last_digit = num % 10

# # if last_digit % 3 == 0:
# # or
# if int(str(num)[-1])%3==0:
#     print("Yes, last digit is divisible by 3")
# else:
#     print("No, last digit is not divisible by 3")





# wap to check the square of integer num is even or odd,
# if even print'hi' else print"hello"

# num = int(input('enter the integer number '))
# if (num**2)%2==0:
#     print('hi')
# else:
#     print('hello')









    # elif



# wap to check the relationship btw two integer number

# num1 = int(input('enter the num1:'))
# num2 = int(input('enter the num2:'))
# if(num1==num2):
#     print('equal')
# elif (num1>num2):
#     print('num1 is greater')
# else:
#     print('lesser')



# wap to check the gvn char is upper or lower or number or special char
# char = (input('enter the num1:'))
# if(char).isupper():
#     print('isupper')
# elif (char).islower():
#     print('islower')
# elif (char).isdigit():
#     print('isnumber')
# else:
#     print('special chracter')


    # wap to check the integer number is having exactly single ordouble or triple or more tn 3
# number = int(input('enter the numb'))
# if len(str(number))==1:
#     print('1 digit')
# elif len(str(number))==2:
#     print('2 digit')
# elif len(str(number))==3:
#     print('3 digit')
# else:
#     print('more')




# take a string input
# if the string having exactly 5 char print the given input
# lessthan 5 print reverse
# more tn 5 print alternative

# text = input("Enter a string: ")

# if len(text) == 5:
#     print(text)
# elif len(text) < 5:
#     print(text[::-1])
# else:  
#     print(text[::2])  












# nested if

# wap to check the given chacter is vowel or not
# char = input('Enter a character: ')

# if char.isalpha():
#     if char in 'aeiouAEIOU':
#         print('It is a vowel.')
#     else:
#         print('It is a consonant.')
# else:
#     print('The character is not an alphabet letter.')


# wap to check pos or neg and even/odd

# number = int(input('enter the no:'))
# if number>0:
#     if number%2==0:
#         print('the no is pos even')
#     else:
#         print('the no is pos odd')
# elif number<0:
#     if number%2==0:
#      print('the no is neg even')
#     else:
#         print('the no is neg odd')
# else:
#     print('the no is 0')





# wap to print the reverse of string only if the string having 
# middle char and startswith vowel n endswith consonanat

string = input('Enter the string: ')

# Check if the length of the string is odd
if len(string) % 2 != 0:
    # Check if the first character is a vowel
    if string[0] in 'AEIOUaeiou':
        # Check if the last character is not a vowel (i.e., it's a consonant)
        if string[-1] not in 'AEIOUaeiou':
            print("Reversed string:", string[::-1])
        else:
            print("The string ends with a vowel, not a consonant.")
    else:
        print("The string does not start with a vowel.")
else:
    print("The string length is not odd.")






