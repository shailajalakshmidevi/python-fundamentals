
## it is the process of duplicating the content of one variable to another variables

## there are 3types

##1. General Copy
##2. Shallow Copy
##3. Deep Copy

###################################################################################

##1. General Copy: it helps to copy the address of source_var to dest_var
## we can use general copy on all the datatype

## syntax:

# source_var = data
# dest_var = source_var

a = 10         ## a is source var and b is dest_var
b = a
print(a, b)
print(id(a), id(b))

list1 = [23, 4.5, 'hii', [9-9j, 8.7, 56]]
list2 = list1
print(list2, list1)
print(id(list2), id(list1))

list1[1] = 5.5
print(list1, list2)

list1[3][0] = 5-9j
print(list1, list2)
print(id(list1[3]), id(list2[3]))

## After General copy, modification WRT one variable will modify the other even the nested collection
## because both the variables will point to the same address

##########################################################################################

##2. Shallow Copy: it is the copy operation, in which the values of source_var will be copied to another
## memory location with differnet address that will get stored wrt dest_var
## we can use this shallow copy on list, set and dict

## syntax:

# source_var = data
# dest_var = source_var.copy()

list1 = [23, 4.5, 'hii', [9-9j, 8.7, 56]]
list2 = list1.copy()
print(list1, list2)

list1[0] = 25
print(list1, list2)
print(id(list1), id(list2))

list1[3][2] = 57
print(list1, list2)
print(id(list2[3]), id(list1[3]))

## After Shallow copy, modification wrt one variable will not modify the other one because the address will be differnt
## but when it comes to nested collection modification wrt one variable will modify the other one because the
## nested collection will have the same address

###################################################################################

##3. Deep copy: it is a copy operation, in which the values of source_var will get duplicated along with the nested collection
## with difffernt address which will get stored wrt to dest var

## synatx:

from copy import deepcopy
# source_var = data
# dest_var = deepcopy(source_var)

list1 = [23, 4.5, 'hii', [9-9j, 8.7, 56]]
list2 = deepcopy(list1)

list1[2] = 'hello'
print(list1, list2)
print(id(list1), id(list2))

list1[3][1] = 9.7
print(list1, list2)
print(id(list1[3]), id(list2[3]))

## After deep copy, modification wrt one variable will not modify the another one even in the nested collection
## because the address of both the collection are completely different






