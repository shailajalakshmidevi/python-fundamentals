
print(dir(str))
## syntax:  variable.attribute()

## capitalize()

string = 'hello good evening'
print(string.capitalize())
string = 'helLo GooD eVenIng'
print(string.capitalize())
string = 'Hello good evening'
print(string.capitalize())
string = 'Hello good evening 12@$'
print(string.capitalize())

## startswith(char/sub-string)

string = 'hello good evening'
print(string.startswith('H'))
print(string.startswith('h'))
print(string.startswith('hello'))

## endswith()

string = 'hello good evening'
print(string.endswith('G'))
print(string.endswith('g'))
print(string.endswith('ing'))

## isalpha()

string = 'hello good evening'
print(string.isalpha())
string = 'hellohii'
print(string.isalpha())
string = 'hellohiiHELLO'
print(string.isalpha())

## isalnum()

string = 'hello good evening'
print(string.isalnum())
string = 'hellohii'
print(string.isalnum())
string = 'hellohiiHELLO123'
print(string.isalnum())
string = '12323433'
print(string.isalnum())

## isdigit()

string = '132424 '
print(string.isdigit())
string = '132424'
print(string.isdigit())
string = '132424a'
print(string.isdigit())

## isspace()

string = 'hello            hii'
print(string.isspace())
string = '                    '
print(string.isspace())

## isupper()

string = 'HEllo HII'
print(string.isupper())
string = 'HELLLO HII'
print(string.isupper())
string = 'HELLLO HII #$565'
print(string.isupper())

## islower()

string = 'HELLO hii'
print(string.islower())
string = 'hello hii $54456'
print(string.islower())

## istitle()

string = 'Hello good evening'
print(string.istitle())
string = 'HellO GooD eVeniNg'
print(string.istitle())
string = 'Hello Good evening'
print(string.istitle())
string = 'Hello Good Evening'
print(string.istitle())
string = 'Hello Good Evening 456$^&'
print(string.istitle())

## upper()

string = 'hello HII'
print(string.upper())
string = 'hello HII 14#$%^'
print(string.upper())

## lower()

string = 'hello HII'
print(string.lower())
string = 'hello HII 14#$%^'
print(string.lower())

## title()

string = 'Hello good evening'
print(string.title())
string = 'HellO GooD eVeniNg'
print(string.title())
string = 'Hello Good evening'
print(string.title())
string = 'Hello Good Evening'
print(string.title())
string = 'Hello Good Evening 456$^&'
print(string.title())

## count(char/sub-string)

string = 'helllo'
print(string.count('l'))
string = 'hellllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllo'
print(string.count('l'))
print(string.count('L'))
string = 'hello hi hi hi hi'
print(string.count('hi'))

## replace(old_string, new_string)

string = 'Good evening'
print(string.replace('Evening', 'Night'))
print(string.replace('evening', 'Night'))
print(string.replace('o', 'O'))

## split()

string = 'hello good evening'
print(string.split())
string = 'hello_good_evening'
print(string.split('_'))
print(string.split('v'))

## strip()

string = '                               hello   hii                         '
print(string)
print(string.strip())
string = '###############################hello#############################'
print(string.strip('#'))

## lstrip()

string = '                               hello   hii                         '
print(string)
print(string.lstrip())
string = '###############################hello#############################'
print(string.lstrip('#'))

## rstrip()

string = '                               hello   hii                         '
print(string)
print(string.rstrip())
string = '###############################hello#############################'
print(string.rstrip('#'))

## index(char), rindex(char)

string = 'hellllo'
print(string[1])           ## indexing: it helps fetch the char at given position
print(string.index('e'))   ## index(): it helps to fetch the index position of given character
print(string.index('l'))   ## index(): it always gets the lowest index position
print(string.rindex('l'))  ## rindex(): it always get the highest index position
print(string.rindex('e'))
# print(string.index('L'))
# print(string.rindex('L'))

## find() and rfind()

string = 'hello'
print(string.find('h'))
print(string.find('l'))           ## find(): it always gets the lowest index position
print(string.rfind('l'))          ## rfind(): it always get the highest index position
print(string.rfind('h'))
print(string.find('P'))
print(string.rfind('U'))

print(bool(''))                   ## the default value of string is '' which is False internally
print(bool(' '))

## variable[index] = new_value

string = 'python'
# string[1] = 'Y'         ## string are immutable in nature() we can't modify the original collection

string = 'python'
print(string.upper())
print(string)

res = string.upper()
print(res)

out = string.replace('y', 'Y')
print(out)
print(string)