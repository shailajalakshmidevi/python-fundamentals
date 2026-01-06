# filter: which helps to filter the particular data from a collection 
# syntax: var = filter(fname,collection)
# print(list(var))



# wap to extract all the strings from the tuple

# print(list(filter(lambda data:type(data)== str,(12,'hi','hello'))))



# wap to extract all the integer number from the collection only if the number having 3 digits

# print(list(filter(lambda data: type(data) == int and len(str(data)) == 3, [12, 'hi', 'hello', 345, 890])))


# wap to get all palandrom numbers in the range 10 to 100


# print(list(filter(lambda num : str(num)==str(num)[::-1],range(10,101))))

# or
# print(list(filter(lambda num : num%11==0,range(10,101))))



# filter strings that are all lowercase

# list_ =['hello','WORLD','python']
# print(list(filter(lambda string : string.islower(),list_)))


# filter booktitles with python

# books = ['Learn python','datascience','python cookbook']
# print(list(filter(lambda string : 'python' in string,books)))




# filter older tn 18
people =[{'name':'tom','age':17},{'name':'tat','age':19}]
print(list(filter(lambda item:item['age']>18, people)))



# filter valid phno 10 digits
no = ['1234567890','322343','3435465656']

print(list(filter(lambda string: len(string) == 10 and string.isdigit(), no)))
