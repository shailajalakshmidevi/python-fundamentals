
## it is the collection of key and value pair enclosed between {}

## syntax:  var = {k1:v1, k2:v2,......}      ## k1, k2 are the keys whereas v1, v2 are the values

dict1 = {1:2.3, 8-9j:23, False:6-8j, 4.5:True}
print(type(dict1))

dict1 = {1:2.3, 8-9j:23, False:6-8j, 4.5:True, 'hii':90, (4,5):'hello', 88:[5,6]}
print(type(dict1))

# dict1 = {1:2.3, 8-9j:23, False:6-8j, 4.5:True, 'hii':90, (4,5):'hello', 88:[5,6], [44,55]:90}
# print(type(dict1))

## the keys should always be immutable in nature, whereas value can be anything

dict1 = {'hii':'hello'}
print(type(dict1))

dict2 = {1:2, 3:4, 5:1, 6:2, 7:1}
print(dict2)
print(len(dict2))

dict3 = {1:2, 3:4, 1:5, 3:6, 7:8, 7:9}
print(dict3)

## we can't have the duplicate keys, if we try to add the duplicates it will override the previous value with the latest value
## whereas the value can be duplicate

## we can't use indexing on dict, instead we use keys to fetch the value
## syntax: variable[key]    ==> lookup syntax

dict2 = {1:2, 3:4, 5:1, 6:2, 7:1}
# print(dict2[2])
print(dict2[5])
print(dict2[7])

## variable[key] = new_value

dict2 = {1:2, 3:4, 5:1, 6:2, 7:1}
dict2[3] = 40                    ## dicts are mutable in nature
print(dict2)
dict2[6] = 90
print(dict2)
dict2[10] = 100
print(dict2)

print(bool({}))         ## the default value of dict is {} which is internally boolean False

print(dir(dict2))

## keys(), values(), items()

dict2 = {1:2, 3:4, 5:1, 6:2, 7:1}
print(dict2)
print(dict2.keys())
print(dict2.values())
print(dict2.items())

## update()

dict2 = {1:2, 3:4, 5:1, 6:2, 7:1}
dict2.update({11:22})
print(dict2)
dict2.update({1:80})
print(dict2)
dict2.update({4:5, 'hii':(5,6)})
print(dict2)

## pop(key)

dict3 = {1: 80, 3: 4, 5: 1, 6: 2, 7: 1, 11: 22, 4: 5, 'hii': (5, 6)}
print(dict3.pop(3))
print(dict3)
print(dict3.pop(11))
print(dict3)
# print(dict3.pop())

## popitem()

dict3 = {1: 80, 3: 4, 5: 1, 6: 2, 7: 1, 11: 22, 4: 5, 'hii': (5, 6)}
print(dict3.popitem())
print(dict3)
print(dict3.popitem())
print(dict3)
print(dict3.popitem())
print(dict3)

## get()

dict3 = {1: 80, 3: 4, 5: 1, 6: 2, 7: 1, 11: 22, 4: 5, 'hii': (5, 6)}
print(dict3[6])
# print(dict3[90])

print(dict3.get('hii'))
print(dict3.get(1))
print(dict3.get(45))
print(dict3.get(45, 'key not found'))
print(dict3.get(45, 0))
print(dict3.get(5, 'key not found'))
print(dict3.get(46, 4))

##################################################################################

dict5 = {34:'program', 8.9:[34, 55.5, ('evening'), ('night',)], 'hii':(400, '456'), 45:{4.5:{900:['py']}}}
print(dict5[8.9][0])
print(dict5[34][2])
print(dict5['hii'][1][1])
print(dict5[8.9][2][1])
print(dict5[8.9][3][0][2])
print(dict5[45][4.5][900][0][0])









