string1 = 'python.py'
print(string1[2:6])
print(string1[1:7+1:2])
print(string1[::-1])
print(string1[4-1:1-1:-1])
print(string1[::2])

#2
string = "Hi Welcome to python"
print(string[::2])
print(string[::-2])
print(string[::-1])
filename = 'Youtube.txt'
url = 'https://google.com'
print(filename[-3:])
print(filename[:7])
print(url[:5])
print(url[8:])

#3
tuple_ = ('selenium', 'manual', [45, 89.9, 'webtech', ['python', 'good', 'evening']], 'sql')
print(tuple_[0][2:5])
print(tuple_[0][1:4])
print(tuple_[2][3][0][::-1])
print(tuple_[2][3][2][::2])
print(tuple_[2][2][::-2])
print(tuple_[2][1:3])
print(tuple_[2])
print(tuple_[2][3][::-1])
print(tuple_[2][3][1:])
print(tuple_[-1][::-1])
print(tuple_[1][1:6:2])
print(tuple_[1][1:3+1])
print(tuple_[1][2:-2+1])

#4
names = ['apple', 'google', 'yahoo', 'amazon', 'facebook', 'instagram', 'microsoft']
print(names[::-1])
print(names[2][3])
print(names[-2:3])
print(names[-6:5])
print(names[-1:2:-1])
# print(names[13])
#output
# ['microsoft', 'instagram', 'facebook', 'amazon', 'yahoo', 'google', 'apple']
# o
# []
# ['google', 'yahoo', 'amazon', 'facebook']
# ['microsoft', 'instagram', 'facebook', 'amazon']
# Traceback (most recent call last):
#   File "/Users/admin/Desktop/qsp/f1/exam.py", line 43, in <module>
#     print(names[13])
#           ~~~~~^^^^
# IndexError: list index out of range


#5
d = {
    'a': 10,
    'b': [1, 2, 'hello', 'python'],
    'c': {
        'd': [(1, 2), ['good morning', 23, 8+9j, 76]]
    },
    'p': {1, 2, 3}
}
print(d['b'][2][::-1])
print(d['c']['d'][1][0][::-2])
print(d['p'])
print(d['b'][3][::2])
print(d['c']['d'][1])
print(d['c']['d'][1][::-1])

#6
dict_ = {
    'key1': ['have a good day', 78, 90.9],
    'key2': (45-9j, 'good night', 990, ['python_py']),
    9: 'hello_hii'
}
print(dict_['key1'][::-1])
print(dict_['key2'][:2])
print(dict_[9][::-2])
print(dict_['key1'][0][3::2])
print(dict_['key1'][1:])
print(dict_['key2'][3][0][::-1])


dict ={'a':'b',1:2,11:22}
# print(int(dict))
# print(float(dict ))
# print(complex(dict ))
print(bool({}))
print(list(dict ))
print(tuple((dict )))
print(set(dict ))
# print(dict(list))
