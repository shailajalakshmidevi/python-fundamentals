
list_ = [12, 3.4, 'hii', 6, 9-9j]         ## iterable
# print(list_)
# print(type(list_))

# for element in list_:
#     print(element)

# print(list_[0], list_[1], list_[2])


## Iterator: it is an object, which helps to traverse through the collection without storing it in the memory
## iter(): it is a function which helps to convert the iterable to iterator
## syntax:    iter_var = iter(col_var)            or         iter_var = col_var.__iter__()

iter_list = iter(list_)               ## iterator
# print(iter_list)
# print(type(iter_list))

# for element in iter_list:
#     print(element)

## next(): it is the function, which helps to get the value one by one from the iterator
## syntax:   next(iter_var)        or      iter_var.__next__()

# print(next(iter_list))
# print(next(iter_list))
# print(iter_list.__next__())
# print(iter_list.__next__())
# print(iter_list.__next__())
# print(next(iter_list))

## when we get the StopIteration Error we must understand the iterator is already been exhausted

# print(iter_list.__next__())
# print(next(iter_list))

# for ele in iter_list:          ## it will give the remaining element from the iterator not from the start
#     print(ele)

## Differences between Iterable and Iterator

## Iterable

## The values of the iterable will get stored in the memory
# print(dir(list_))
## It consist of only __iter__() attribute in it
## we can iterate n number of times
## we can use the len() on iterable because of the attribute __len__()
## print(len(list_))         or  print(list_.__len__())
## we can use indexing on iterable becaue of the attribute __getitem__()
## print(list_[0], list_[1], list_[2])   or        print(list_.__getitem__(0))


## Iterator

## The values of the ierator will not get stored in the memory it just creates the object
# print(dir(iter_list))
## It consist of __iter__() and __next__() attribute in it
## we can iterate only one, If we try to iterate multiple time we get the Error "Stopiteration"
## we can't use the len() because we don't have the attribute __len__()
# print(len(iter_list))
## we can't use indexing on iterator because we don't have the attribute __getitem__()
## print(iter_list[0])

# iter1 = iter(iter_list)
# print(iter1)

## we can convert the iterables to iterator but reverse is not True

###################################################################################################

def Sam():
    return 1
    return 2
    return 3
# print(Sam())

def Demo():
    print('hello')
    return 'hii'
    print('This is python class')
    return 'byee'
# print(Demo())

## Generator: it is an inbuilt iterator, which helps to create the sequence
## here instead of "return" we use "yield" keyword

def Demo1():
    yield 1
    yield 'hii'
    yield 2
# print(Demo1())

# result = Demo1()
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))          ## we already accessed all the element so we get error for this print statement

##or

# print(tuple(Demo1()))

## WAP TO GET ALL THE EVEN NUMBERS FROM THE LIST USING GENERATOR
# list_ = [1,2,3,4,5,6,7]  out = [2,4,6]

def Get_Even_Num(list_):
    for num in list_:
        if num % 2 == 0:
            yield num
# print(list(Get_Even_Num([1,2,3,4,5,6,7,8,9])))

## Generator expression

# list_ = [1,2,3,4,5,6,7]
# print(list(num for num in list_ if num % 2 == 0))

## WAP TO YIELD ALL THE STRING WHICH STARTS WITH VOWEL
list_ = ['apple', 'google', 'ajio', 'youtube', 'insta', 'amazon', 'gmail']

def Get_String(list_):
    for string in list_:
        if string[0] in 'aeiouAEIOU':
            yield string
# print(list(Get_String(list_)))

##or

# print(list(string for string in list_ if string[0] in 'AEIOUaeiou'))

## WAP TO GET THE FOLLOWING OUTPUT
list_ = [4.5, 77, 'python', 5-8j, 'java']
# out: {'python':'pn', 'java':'ja'}

def Create_Dict(list_):
    for element in list_:
        if type(element) == str:
            yield element, element[0] + element[-1]
# print(dict(Create_Dict(list_)))

##or

# print(dict((element, element[0] + element[-1]) for element in list_ if type(element) == str))

# Generator to yield only vowels from a string

def get_vowel(string):
    for char in string:
        if char in 'AEIOUaeiou':
            yield char
# print(list(get_vowel('hello hii good evening')))

##or
# string = 'hello hii good evening'
# print(list(char for char in string if char in 'AEIOUaeiou'))

# Generator to yield word and length of word
string = 'hello hii good morning'

def Word_Length(string):
    for word in string.split():
        yield word, len(word)
print(dict(Word_Length('hello hii good morning')))

##or

print(dict((word, len(word)) for word in string.split()))




