
## it is a collection homogenous or hetrogenous data item enclosed inside the {}

## var = {val1, val2,......}

set1 = {1, 3.4, 6-8j, False}
print(type(set1))

set1 = {1, 3.4, 6-8j, False, 'hii', (1,2)}
print(type(set1))

# set1 = {1, 3.4, 6-8j, False, 'hii', (1,2), [1,2,3]}
# print(type(set1))

# set1 = {1, 3.4, 6-8j, False, 'hii', (1,2), {1,2,3}}
# print(type(set1))

## we can't have mutable data item(list, set, dict) inside the set

set1 = {1, 3.4, 6-8j, False, 'hii', (1,2), (1,2,3), 'hello'}
print(set1)

## sets are unordered in nature so can't use indexing on set type

set2 = {1,1,1,1,1,2,2,3,3,3,5,5,5,7,8,5}
print(set2)

## sets doesn't allow us to store the duplicate value

print(bool(set()))            ## The default value for set is set() which is internally boolean False

print(dir(set))

## add()

set1 = {1, 3.4, 6-8j, False}
data = (11,5.6, 90-9j)
set1.add(200)
print(set1)
set1.add('hello')
print(set1)
set1.add(data)
print(set1)

## update()

set1 = {1, 3.4, 6-8j, False}
data = [11,5.6, 90-9j]
# set1.update(300)
set1.update('python')
print(set1)
set1.update(data)
print(set1)

## pop()

set4 = {False, 1, 3.4, 'h', 5.6, 'y', 'n', 11, (6-8j), 'o', 'p', 't', (90-9j), 'b'}
print(set4.pop())
print(set4)
print(set4.pop())
print(set4)
print(set4.pop())
print(set4)

## remove(value)

set4 = {False, 1, 3.4, 'h', 5.6, 'y', 'n', 11, (6-8j), 'o', 'p', 't', (90-9j), 'b'}
set4.remove(1)
print(set4)
set4.remove(5.6)
print(set4)
# set4.remove(900)

## discard(value)

set4 = {False, 1, 3.4, 'h', 5.6, 'y', 'n', 11, (6-8j), 'o', 'p', 't', (90-9j), 'b'}
set4.discard(11)
print(set4)
set4.discard('o')
print(set4)
set4.discard('abc')
print(set4)

## note:
## remove() throw the error when we try to remove the elemnet which is not present in the set
## discard() will not throw error it ignores

## isdisjoint()

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2))

set1 = {1,2,3,7}
set2 = {4,5,6,2}
print(set1.isdisjoint(set2))

## issubset():  base_set.issubset(ref_set)

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.issubset(set2))

set1 = {1,2,3}
set2 = {4,5,6,1,2}
print(set1.issubset(set2))

set1 = {1,2,3}
set2 = {4,5,6,1,2,3}
print(set1.issubset(set2))

## issuperset()

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.issuperset(set2))

set1 = {1,2,3,4,5,6}
set2 = {4,5,6}
print(set1.issuperset(set2))

## union()

set1 = {1,2,3}
set2 = {4,5,6}
res = set1.union(set2)
print(res)
print(set1, set2)

## intersection()

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.intersection(set2))

set1 = {1,2,3,4}
set2 = {4,5,6,3}
print(set1.intersection(set2))
print(set1, set2)

## intersection_update()

set1 = {1,2,3}
set2 = {4,5,6}
set2.intersection_update(set1)
print(set1, set2)

set1 = {1,2,3,4}
set2 = {4,5,6,3}
set1.intersection_update(set2)
print(set2, set1)

## difference()

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.difference(set2))

set1 = {1,2,3,7,8,9}
set2 = {4,5,6}
print(set1.difference(set2))

set1 = {1,2,3}
set2 = {4,5,6,1,2}
print(set1.difference(set2))

set1 = {1,2,3}
set2 = {4,5,6,1,2}
print(set2.difference(set1))
print(set1, set2)

## difference_update()

set1 = {1,2,3}
set2 = {4,5,6,1,2}
set2.difference_update(set1)
print(set1, set2)

set1 = {1,2,3}
set2 = {4,5,6,1,2}
set1.difference_update(set2)
print(set2, set1)

## symmetric_differnce()

set1 = {1,2,3}
set2 = {4,5,6,1,2}
print(set1.symmetric_difference(set2))
print(set1, set2)

## symmetric_differnce_update()

set1 = {1,2,3}
set2 = {4,5,6,1,2}
set2.symmetric_difference_update(set1)
print(set1, set2)