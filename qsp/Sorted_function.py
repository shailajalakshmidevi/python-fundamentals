
## sorted(): it is a function which helps to arrange the elements in the order
## it will not modify the original collection, always we get the list output

## sorting the list
list_ = [132, 34463424, 12453463453,3, 12435, 1, 456765434567]
print(sorted(list_))
print(sorted(list_, reverse = True))
print(list_)

## sorting the tuple

tuple_ = (132, 34463424, 12453463453,3, 12435, 1, 456765434567)
print(sorted(tuple_))
print(sorted(tuple_, reverse = True))
print(tuple_)

## sorting the string

string = 'python'
print(sorted(string))
print(sorted(string, reverse = True))

## sorting the set

set_ = {132, 34463424, 12453463453,3, 12435, 1, 456765434567}
print(sorted(set_))
print(sorted(set_, reverse = True))
print(set_)

## sorting the dict

dict_ = {'g':56, 'z':800, 'm':4, 'a':1}
# print(sorted(dict_))
# print(sorted(dict_.values()))
# print(sorted(dict_.items()))

#######################################################################################

## sorting the list of string based on the length
list_ = ['apple', 'youtube', 'gmailllllllllllllllllllllll', 'instaaaaaa']
# print(sorted(list_))
# print(sorted(list_, key = len))
# print(sorted(list_, key = len, reverse = True))

##2. sorting the list based on last character of the string
list_ = ['bv', 'aw', 'dt', 'cu']
# print(sorted(list_))
# print(sorted(list_, reverse = True))
# print(sorted(list_, key = lambda item:item[-1]))

##3. sorting the list based on the temperature
temperatures = [('bangalore', 39), ('delhi',40), ('chennai', 38), ('mumbai', 41)]
# print(sorted(temperatures))
# print(sorted(temperatures, key = lambda item: item[1]))

#4. sorting the list based on the first element of inner list
list_ = [[2,6], [7,3], [3,8], [8,7], [9,7], [4,9]]
# print(sorted(list_))
# print(sorted(list_, key = lambda item: item[0]))

#5. sorting the list based on the last element of inner list
list_ = [[2,6], [7,3], [3,8], [8,7], [9,7], [4,9]]
# print(sorted(list_, key = lambda item: item[1]))

##6. sorting the dict based on values
dict_ = {'a':4, 'b':3, 'c':1, 'd':9}
# print(sorted(dict_))
# print(sorted(dict_.items()))
# print(sorted(dict_.items(), key = lambda item:item[1]))

##7. find the longest substring
string = 'this is programming language and programming is fun'
word_length = {word: len(word) for word in string.split()}
print(word_length)
print(sorted(word_length.items(), key = lambda item: item[-1]))
print(sorted(word_length.items(), key = lambda item: item[-1])[-1])
print(sorted(word_length.items(), key = lambda item: item[-1])[-1][0])

##8. find the most repeated word in given string
string = 'hii helllo hii hii hello good evening good morning hii hii'








