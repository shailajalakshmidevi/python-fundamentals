
# lambda: it is which keyword, it is the shortest form of function

## syntax:

# var = lambda args: expression
# print(var(value))

## WAP to add 20 to the given integer number

add_20 = lambda number: number + 20
# print(add_20(20))

## WAP TO GET THE SQUARE AND CUBE OF THE GIVEN NUMBER

sqaure_cube = lambda number: (number ** 2, number ** 3)
# print(sqaure_cube(2))

## WAP TO GET THE LAST CHARACTER OF THE STRING

last_char = lambda string: string[-1]
# print(last_char('hello'))

## WAP TO CHECK THE STRING IS PALINDROME OR NOT

check_palindrome = lambda string: string == string[::-1]
# print(check_palindrome('mom'))

## WAP TO CHECK THE CHARACTER PRESENT IN STRING OR NOT

check_char = lambda string, char: char in string
# print(check_char('good', 'o'))

## WAP TO RETURN THE SUM OF NUMBERS TILL n

Get_Sum = lambda number: sum(range(number + 1))
# print(Get_Sum(4))

## WAPT TO RETURN LAST n ELEMENT FROM THE COLLECTION

last_n_element = lambda collection, num: collection[-num:]
# print(last_n_element('python', 3))
# print(last_n_element([1,2,3,4,5,6,7,8,9], 5))

## syntax for lambda expression when we have conditions to check

# var = lambda args:'TSB' if condition else 'FSB'
# print(var(value))

## WAP TO CHECK THE GIVEN NUMBER IS EVEN OR NOT

check_even_odd = lambda number:'EVEN' if number % 2 == 0 else 'ODD'
# print(check_even_odd(23))

## WAP TO PRINT THE ASCII VALUE OF THE CHARACTER IF IS LOWERCASE
# ELSE GET THE REVERSE OF THE ACSII VALUE

check_lowercase = lambda char:ord(char) if char.islower() else int(str(ord(char))[::-1])
# print(check_lowercase('A'))

## WAP TO CHECK THE GIVEN STRING IS KEYWORD OR NOT

import keyword
check_for_Keyword = lambda string:'Keyword' if string in keyword.kwlist else 'Not Keyword'
# print(check_for_Keyword('lambda'))

#############################################################################################

## map: it is a function, which helps to execute the same set of instruction s to each and every element og the collection

## syntax:

# var = map(fname, collections)
# print(list(var))

## WAP TO SQUARE AND CUBE EACH AND EVERY ELEMENT IN THE GIVEN LIST
# list_ = [1,2,3,4] ===> out = [[1, 1], [4, 8], [9, 27], [16, 64]]

def square_cube_(list_):
    out = []
    for num in list_:
        out.append([num ** 2, num ** 3])
    return out
# print(square_cube_([1,2,3,4]))

##or

Square_Cube = lambda number: [number ** 2, number ** 3]
res = map(Square_Cube, [1,2,3,4])
# print(list(res))

##or

# print(list(map(lambda number: [number ** 2, number ** 3], [1,2,3,4])))

## wap to convert the negative number to positive number
# whereas positive number should reamins the same from the given list,
# get the maximun and minimum value from the list
# list_ = [1, 3, -6, -88, -67]   out = [1,3,6,88,67] min: 1, max : 88

# print(list(map(lambda number: abs(number), [1, 3, -6, -88, -67])))
# print(max(list(map(lambda number: abs(number), [1, 3, -6, -88, -67]))))
# print(min(list(map(lambda number: abs(number), [1, 3, -6, -88, -67]))))

## WAP TO GET THE FOLLOWING OUTPUT
# LIST_ = [123, 34, 24, 512]
# OUT = [6, 7, 6, 8]

def get_sum(number):
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)
    return sum_digit

# print(list(map(get_sum, [123, 34, 24, 512])))

##or

# print(list(map(lambda number: sum([int(digit) for digit in str(number)]), [123, 34, 24, 512])))

# WAP TO GET THE FOLLOWING OUTPUT
list_ = [56, 8.7, [1,2,4], 'helloo', 9-9j, [1,2,3,4]]
# out = [1, 1, 3, 6, 1, 4]
# print(list(map(lambda data:1 if type(data) in [int, float, complex, bool] else len(data), list_)))

## Convert list of strings to uppercase
list_ = ['Hello', 'hii', 'how are you']
# print(list(map(lambda string: string.upper(), list_)))

#Convert list of strings to integers
list_ = ['1', '2', '34', '4567', '56789']
print(list(map(lambda string: int(string), list_)))

## Strip whitespace from strings
raw_strings = ['  apple  ', ' banana ', 'cherry  ']    ## out =  ['apple', 'banana', 'cherry']
print(list(map(lambda string: string.strip(), raw_strings)))

## Prefix each item with its index using enumerate
items = ['apple', 'banana', 'cherry']             ## out = {0: 'apple', 1: 'banana', 2: 'cherry'}

##WAP TO GET THE FOLLOWING OUTPUT
string = 'hii hello how are you'
# out = [3, 5, 3, 3, 3]

# Add two lists element-wise using zip()
a = [1, 2, 3]
b = [4, 5, 6]

######################################################################################

## filter: it is function which helps to filter the particular data item from the collection

## syntax:

# var = filter(fname, collections)
# print(list(var))

##WAP TO EXTRACT ALL THE STRINGS FROM THE TUPLE

# print(list(filter(lambda data: type(data) == str, (12, 'hii', 'hello', 90.78))))

## WAP TO EXTRACT ALL THE INTEGER NUMBER FROM THE COLLECTION ONLY IF THE NUMBER HAVING 3 DIGITS

# print(list(filter(lambda data: type(data) == int and len(str(data)) == 3, [111, 4444, 5, 777, 'hii'])))

## WAP TO GET ALL THE PALINDROME NUMBERS IN THE RANGE 10 TO 100

# print(list(filter(lambda num: str(num) == str(num)[::-1], range(10, 101))))
# print(list(filter(lambda num: num % 11 == 0, range(10, 101))))

## Filter strings that are all lowercase.
list_ =['hello', 'WORLD', 'Python']
# print(list(filter(lambda string: string.islower(), list_)))

## Filter Book titles with "Python"
books = ['Learn Python', 'Data Science', 'Python Cookbook', 'python Cookbook']
# print(list(filter(lambda string: 'Python' in string, books)))

## Filter People older than 18
people = [{'name': 'Tom', 'age': 17}, {'name': 'Anna', 'age': 21}]
# print(list(filter(lambda item: item['age'] > 18, people)))

## Filter Valid phone numbers (10 digits)
numbers = ['1234567890', '98765', '123456789a']
print(list(filter(lambda string: len(string) == 10 and string.isdigit(), numbers)))





