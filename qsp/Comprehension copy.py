
## List Comprehension: it helps to create the new list in the single line

## syntax:

##1. var = [exp for variable in collections]

##2. var = [exp for variable in  collections if condition]

##3. var = [exp1 if condition else exp2 for variable in collections]


## WAP TO GET THE SQUARE OF INDIVIDUAL NUMBER IN THE GIVEN LIST
list_ = [1,2,3,4,5,6]      ## [1,4,9,16,25,36]
out = []
for num in list_:
    out.append(num ** 2)
# print(out)

##or

res = [num ** 2 for num in list_]
# print(res)

##or

# print([num ** 2 for num in list_])

## WAP TO GET THE CUBE OF INDIVIDUAL NUMBER ONLY IF THE NUMBER IS EVEN IN THE GIVEN LIST
list_ = [1,2,3,4,5,6]
print([num ** 3 for num in list_ if num % 2 == 0])

## WAP TO GET THE FOLLOWING OUTPUT
list_ = [1, 2, 3, 4]
# out = [1, 2, 9, 64]
print([list_[index] ** index for index in range(len(list_))])

## WAP TO CREATE A LIST OF NUMBER WHICH IS DIVISIBLE BY 3
LIST_ = [4,6,4,5,73,8,3,7,9,44]
print([num for num in LIST_ if num % 3 == 0])

## WAP TO EXTRACT ALL THE NUMBER WHOSE LAST 2 DIGITS ARE DIVISIBLE BY 4
list_ = [444, 448, 1096, 1908, 1234, 575]
print([num for num in list_ if (num  % 100) % 4 == 0])

##or

print([num for num in list_ if int(str(num)[-2:]) %  4 == 0])

## TAKE A STRING INPUT, IF THE LENGTH WORD IS EVEN GET THE STRING AS IS ELSE GET THE REVERSE STRING
string = 'hello hiii good morning'
print([word if len(word) % 2 == 0 else word[::-1] for word in string.split()])

## get the string having less than equal 4 char and endswith e
names = ["John", "Jane", "Mike", "Anna", "James", "Mary"]
print([string for string in names if len(string) <= 4 and string.endswith('e')])

##or

print([string for string in names if len(string) <= 4 if string.endswith('e')])

## WAP TO CREATE THE LIST OF ONLY THOSE KEYS OF DICT WHOSE VALUE IS EVEN
dict_ = {'a':1, 'b':2, 'c':3, 'd':4}      #out = ['b', 'd']
print([key for key, value in dict_.items() if value % 2 == 0])

##or

print([key for key in dict_ if dict_[key] % 2 == 0])

###################################################################################

## set comprehension: it helps to create new set

## syntax:

##1. var = {exp for variable in collections}

##2. var = {exp for variable in  collections if condition}

##3. var = {exp1 if condition else exp2 for variable in collections}

##1. WAP TO GET THE FOLLOWING OUTPUT
string = 'this is python session'
#  out = {('this', 4), ('is', 2), ('python', 6), ('session', 7)}
print({(word, len(word)) for word in string.split()})

##2. Wap to get all the vowels in the given string
string = 'this is python session'
print({char for char in string if char in 'aeiouAEIOU'})

##3. take a list integer number, if the number is even get square else get cube
list_ = [1,2,3,4,5,6,7,8,9]
print({num ** 2 if num % 2 == 0 else num ** 3 for num in list_})

## WAP TO CREATE A NEW SET, WHICH CONSIST OF NAMES STRATS WITH CONSONENTS
NAMES = ['APPLE', 'YOUTUBE', 'EMAIL', 'GMAIL', 'YAHOO']

## WAP TO CREATE A SET, WHICH CONSIST OF ONLY STRING HAVING LESS THAN 5 CHARACTER
NAMES = ['APPLE', 'YOUTUBE', 'EMAIL', 'GMAIL', 'YAHOO', 'HII', 'Ajio']

############################################################################################

## dict comprehenion: it helps to create new dict

## syntax:

##1. var = {k:v for variable in collections}

##2. var = {k:v for variable in  collections if condition}

##3. var = {k:v if condition else v for variable in collections}

##1. WAP TO CREATE THE DICTIONARY OF WORD AND LENGTH PAIR
NAMES = ['APPLE', 'YOUTUBE', 'EMAIL', 'GMAIL', 'YAHOO']
print({name: len(name) for name in NAMES})

##2. WAP TO GET THE FOLLOWING OUTPUT
string = 'python java selenium webtech sql web ja'
# out: {'python': 'nohtyp', 'java':'avaj', 'selenium':  'muineles', 'ja':'aj'}
print({word: word[::-1] for word in string.split() if len(word) % 2 == 0})

##2. WAP TO GET THE FOLLOWING OUTPUT
string = 'python java selenium webtech sql web ja'
# out: {'python': 'nohtyp', 'java':'avaj', 'selenium':  'muineles', 'webtech': 7, 'sql': 3, 'web':3, ja':'aj'}

##3. WAP TO THE FOLLOWING OUTPUT
DICT_ = {'a':1, 'b':2, 'c':3}
# out: {1: 'a', 2: 'b', 3: 'c'}








