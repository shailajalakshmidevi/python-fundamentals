print(bool(set()))
print(bool([]))

set1 = {1,2,45,False}
set1.update('python')
print(set1)

set1 = {1,2,45,False}
data = [11,2,3]
set1.update('python')
print(set1)

set1 = {1,2,45,False}
set1.pop()
print(set1)
#set1.remove(45)
set1.pop()
print(set1)

print(set1)
 
#isdisjoint()

set1 = {1,2,3}
set2 = {22,23,4}
print(set1.isdisjoint(set2))