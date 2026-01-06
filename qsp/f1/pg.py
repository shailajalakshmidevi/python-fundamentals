print(dir(str))
# syntax = variable.attribute
# CAPITALIZE()
STRING = "HELLO"
print(STRING.capitalize())
STRING = "hello1122333"
print(STRING.capitalize())
TRING = "Hello"
print(STRING.capitalize())

# startwith
STRING = "HELLO"
print(STRING.startswith('h'))
#endswith
STRING = "HELLO"
print(STRING.endswith('O'))
#istitile
STRING = "HELLO e3rr44466"
print(STRING.istitle())
#title
STRING = "HELLO 465475787887"
print(STRING.title())
#count
STRING = "HELLO"
print(STRING.endswith('O'))
#REPLACE
STRING = "HELLO"
print(STRING.replace('H','h'))
#SPLIT
STRING = "HELLO morning"
print(STRING.split())
STRING = "HELLO_morning"
print(STRING.split())
#strip
STRING = "                            HELLO  morning           "
print(STRING.strip())
STRING = "                            ####HELLO  morning           "
print(STRING.strip('#'))
STRING = " HELLO  morning           "
print(STRING.lstrip())
STRING = "HELLO  morning"
print(STRING.index('m'))
STRING = "HELLO  morning"
print(STRING.index('L'))
STRING = "HELLO  morning"
print(STRING.rindex('L')) 
#rindex displays max index value

#find and rfind
STRING = "HELLO  morning"
print(STRING.find('L'))
STRING = "HELLO  morning"
print(STRING.rfind('L'))
#default value of string '' is boolean false

print(bool(''))
print(bool(' ')) #ll gv true

#variable[index]= new_value
# string = 'python'
# string[1] = 'y'## string are immutable in nature we cant modify the original callection
string = 'python'
print(string.upper())
print(string)#there is no change or conversion
 #extend list

list =[1,2,3]
data = (11,2,22)
list.extend("1223")
list.extend(data)
print(list)


list =[1,2,3]
list.sort(reverse=True)
print(list)

list =[12,'hello',['python',560,6.6,['sql'],'webtech',900]]
print(list[1])
print(list[1][3])
print(list[2][1])
print(list[2][0][1])


######variable[index] = new_value

#lista aree mutable it allows modify the original collection

list =['1,2,3']
print (list) 