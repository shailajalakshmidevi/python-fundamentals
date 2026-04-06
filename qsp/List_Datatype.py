
# it is collection of homogenous or hetrogenous data item enclosed inside the []

## syntax:  var = [val1, val2,.....]

list1 = [1,2,3,4,5]                ## Homogenous list
list2 = [1, 2.3, 9-9j, True]       ## Hetrogenous list
print(type(list2))
print(len(list1), len(list2))

print(bool([]))                  ## The default value of list is [] which is internally boolean False

print(dir(list2))

## append()
list2 = [1, 2.3, 9-9j, True]
data = (11,22,33)
list2.append(200)
print(list2)
list2.append('hello')
print(list2)
list2.append(7.9)
print(list2)
list2.append(data)
print(list2)
list2.append("123")
print(list2)

## extend()
list2 = [1, 2.3, 9-9j, True]
data = (11,22,33)
# list2.extend(233)
list2.extend("1234")
print(list2)
list2.extend(data)
print(list2)

## Note:
##1. append() accept both sVD and MVD where as the extend() takes only MVD
##2. addend() adds the collection as is whereas the extend() breaks the collection.

## insert(index_position, value)
list2 = [1, 2.3, 9-9j, True]
list2.insert(0, 300)
print(list2)
list2.insert(4 ,'python')
print(list2)

## pop()

list3 = [1, 2.3, (9-9j), True, '1', '2', '3', '4', 11, 22, 33]
print(list3.pop())
print(list3)
print(list3.pop())
print(list3)
print(list3.pop())
print(list3)

## pop(index)
list3 = [1, 2.3, (9-9j), True, '1', '2', '3', '4', 11, 22, 33]
print(list3.pop(2))
print(list3)
print(list3.pop(4))
print(list3)
print(list3.pop(6))
print(list3)

## remove(value)
list3 = [1, 2.3, (9-9j), True, '1', '2', '3', '4', 11, 22, 33]
list3.remove(1)
print(list3)
list3.remove('1')
print(list3)

## clear()

list3 = [1, 2.3, (9-9j), True, '1', '2', '3', '4', 11, 22, 33]
list3.clear()
print(list3)

## count()

list4 = [1,2,3,1,1,1,1,2,3]
print(list4.count(1))
print(list4.count(123))

## index()
# list4 = [1,2,5,3,1,1,1,1,2,3]
# print(list4.index(1))
# print(list4.index(5))

## reverse()
list4 = [1,2,3,1,1,1,1,2,3, 'hii', 7878-9j, True]
list4.reverse()
print(list4)

## sort()

list5 = [32, 232435,4634657, 34325235, 1, 4556464, 33, 565786]
list5.sort()
print(list5)
list5.sort(reverse = False)
print(list5)
list5.sort(reverse = True)
print(list5)

#############################################################################
## indexing
list6 = [12, 'hello', ['python', 560, 6.6, ['sql']], 'webtech', 900]
print(list6[1])
print(list6[1][3])
print(list6[2][1])
print(list6[2][0][1])
print(list6[2][3][0][1])
print(list6[4])

## index()
list4 = ['1',2,5,3,1,1,1,1,2,3, 5.6]
print(list4.index('1'))
print(list4.index(5.6))
# print(list4.index('8'))

## variable[index] = new_value

list4 = ['1',2,5,3,1,1,1,1,2,3, 5.6]
list4[1] = 200                         ## lists are mutable in nature(it allows us to modify the original collection)
print(list4)


