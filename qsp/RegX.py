
### it helps to fetch the particular data item from the file

## syntax:

# import re
# var = re.findall('exp', 'data')             ## findall returns the list of all the matching records

###########################################################################################
import re

res = re.findall('the', 'the theory of relativity')
print(res)
print(re.findall('cat', 'the dragging belly indicates your cat is too fat'))
print(re.findall('python', 'python and java are object oriented'))
print(re.findall('aeiou', 'python and java are object oriented'))
print(re.findall('smith', 'smith and blackSmith'))
print(re.findall('Smith', 'smith and blackSmith'))

############################################################################################

## character set: it helps to match one in many character

print(re.findall('[sS]mith', 'smith and blackSmith'))

## match grey and gray
print(re.findall('gr[ea]y','match grey and gray'))

## match separate and seperate
print(re.findall('sep[ae]rate','match separate and seperate'))

## match any one in vowel (either a, e, i, o, u)
print(re.findall('[aeiou]', 'hello good evening'))

## match all the numbers
print(re.findall('[0123456789]', 'the book costs 122346 Rs'))

#####################################################################################

## chaarcter "-": it helps to match the character in the range

## match all the numbers
print(re.findall('[0-9]', 'the book costs 122346 Rs'))

## match all the lowercase
print(re.findall('[a-z]', 'the book costs 122346 Rs'))

## match all the lowercase
print(re.findall('[A-Z]', 'the book costs 122346 Rs'))

## match all the lowercase and uppercase
print(re.findall('[A-Za-z]', 'the book costs 122346 Rs'))

#################################################################################################

## character "+": it helps to match 1 to n number of cahacter as long as there is a match

## match all the lowercase as long as ther is a match
print(re.findall('[a-z]+', 'the book costs 122346 Rs'))

## matching all the numbers as long as there is match
print(re.findall('[0-9]+', 'the book costs 122346 Rs and pen costs 10 RS'))

print(re.findall('an+a', 'Hello anna'))

print(re.findall('an+a', 'Hello aa'))

print(re.findall('an+a', 'Hello ana'))

####################################################################################

## character "*": it helps to match 0 to n number of character

print(re.findall('an*a', 'Hello anna'))
print(re.findall('an*a', 'Hello aa'))
print(re.findall('an*a', 'Hello annnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnna'))

####################################################################################

## character ?: it helps to match either 1 or 0 character

print(re.findall('an?a', 'Hello annnnnnnnnnnnnnnnnnnnnnnnna'))
print(re.findall('an?a', 'Hello ana'))
print(re.findall('an?a', 'Hello aa'))

####################################################################################
## negation we use "^"

## get all the character other than digits
print(re.findall('[^0-9]', 'the book costs 122346 Rs and pen costs 10 RS'))

## match all the characters except vowel
print(re.findall('[^aeiou]', 'the book costs 122346 Rs and pen costs 10 RS'))

## match all the charcater as long as there is a match except the numbers
print(re.findall('[^0-9]+', 'the book costs 122346 Rs and pen costs 10 RS'))

####################################################################################

## starting "^": it helps to check the string starts with gievn substring
## ending "$": it checks the string ends wuth given substring

print(re.findall('^hiii','hello hii good evening'))
print(re.findall('^hello','hello hii good evening'))
print(re.findall('hiii$','hello hii good evening'))
print(re.findall('evening$','hello hii good evening'))

####################################################################################

## word boundary(\b): it helps to get the data in the boundary
## word boundary means there must be a transtion between word and non-word character

print(re.findall('day',"what a beautiful day today is"))
print(re.findall(r'\bday',"what a beautiful day today is"))
print(re.findall(r'day\b',"what a beautiful day today is"))
print(re.findall(r'\bday\b',"what a beautiful day today is"))

# Regular expression which matches words that starts with "h"
print(re.findall(r'\bh[a-zA-Z]+','hello world hi hello universe how are you happy birthday'))

# Regular expression which matches words that starts with "P or J"
print(re.findall(r'\b[PJ][a-zA-Z]+', 'Python is a programming language. Python is easier than Java'))

# Regular expression which matches words that ends with "y"
print(re.findall(r'[a-zA-Z]+y\b','hello world hi hello universe how are you happy birthday feeling very sleepy flying'))

# print only those words starting with vowel character
print(re.findall(r'\b[aeiou][a-zA-Z]+', "hello hi american english and indian ocean united states"))

# Matches only Capital Letter words
print(re.findall(r'\b[A-Z]+\b',"This is PYTHON programming LANGUAGE and REGEX"))

# Matching only pdf files
print(re.findall(r'[a-zA-Z]+.pdf\b',"downloading apple.pdf orange.csv grape.pdf ice.txt to downloads folder"))

######################################################################################
## matching digit

print(re.findall('[0123456789]',"654 this string is starting with 12 and ending with numbers 289423784612 890"))
print(re.findall('[0-9]',"654 this string is starting with 12 and ending with numbers 289423784612 890"))
print(re.findall(r'\d',"654 this string is starting with 12 and ending with numbers 289423784612 890"))

## match all the digits as long as there is match
print(re.findall(r'\d+',"654 this string is starting with 12 and ending with numbers 289423784612 890"))

# Matches sequence of all 3 digit pattern
print(re.findall(r'\d{3}',"654 this string is starting with 12 and ending with numbers 289423784612 890"))

# Matches the string that ends with 3 digit number
print(re.findall(r'\b\d{3}\b',"4632746327 this string is ending with 235"))

# Phone Number pattern (4DIGITS-3DIGITS-3DIGITS)
print(re.findall(r'\b\d{4}-\d{3}-\d{3}', 'this is my number 9869-967-234'))










