
# ## these are special symbol which helps to perform some task

# ## there are 6 types

# ##1. Arithmetic Operator
# ##2. Logical Operator
# ##3. Relational Operator
# ##4. Assignment Operator
# ##5. Membership operator
# ##6. Identity Operator

# #######################################################################################

# ##1. Arithmetic Operator

# ##1. Addition Operator:

# print(1 + 1)
# print(1 + 2.3)
print(1 + 9-9j)
# print(1.3 + 4.5)
# print(1.2 + 8-9j)
print(1 + 9j + 8-9j)
# print(True + False)

# print('hii' + 'hello')
print([1,2] + [3,4])
# print((11,22) + (223,))
# # print({1,2} + {3,5})
# # print({1:2} + {4:6})
# print('*************************')

# ## Subtraction

# print(1 - 1)
# print(1 - 2.3)
# print(1 - 9-9j)
# print(1.3 - 4.5)
# print(1.2 - 8-9j)
# print(1 + 9j - 8-9j)
# print(True - False)


# # print('hii' - 'h')
# # print([1,2] - [1])
# # print((1,2) - (3,4))
# # print({1:2} - {2:3})
# print({1,2,3} - {4,5,6})
# print({1,2,3} - {4,5,6,2,3})     ## it will get only the unique element present in the set1
# print('**********************************')

# ## Multiplication(*)

# print(1 * 1)
# print(1 * 2.3)
# print(1 * 9-9j)
# print(1.3 * 4.5)
# print(1.2 * 8-9j)
# print(1 + 9j * 8-9j)
# print(True * False)

# print('hii' * 2)
# print([1,2] * 4)
# print((3,4) * 6)
# # print({2,3} * 7)
# # print({1:2} * 6)
# print('************************************')

# ## Division: the division operators will not support collection datatype

# ##1. True Division(/): it helps to get the exact division output

# print(1 / 1)
# print(1 / 2.3)
# print(1 / 9-9j)
# print(1.3 / 4.5)
# print(1.2 / 8-9j)
# print(1 + 9j / 8-9j)
# print(False / True)
# print('*****************************')

# ##2. Floor Division(//):  it helps to get the exact division output by eliminating float values

# print(1 // 1)
# print(1 //2.3)
# print(1 // 9-9j)
# print(1.3 // 4.5)
# print(1.2 // 8-9j)
# print('******************************')

# ##3. Modulus(%): it helps to get the reminder

# print(1 % 1)
# print(1 % 2.3)
# print(1 % 9-9j)
# print(1.3 % 4.5)
# print(1.2 % 8-9j)
# print(20 % 2)
# print('******************************')


# ## Power(**): it helps to raise the number with specified value
# ## it will not wordk for collection type

# print(1 ** 1)
# print(1 ** 2.3)
# print(1 ** 9-9j)
# print(1.3 ** 4.5)
# print(1.2 ** 8-9j)
# print(1 + 9j ** 8-9j)
# print(True ** False)
# print(2 ** 3)
# print('*************************************')

# ##################################################################################

# ## Logical Operator

# ##1. Logical and(and):

# ##if op1 == True(1) then output == op2
# ##if op1 == False(0) then output == op1

# print(10 and 20)
# print(0 and 1)
# print('hello' and [])
# print(() and '')
# print('********************************')

# ##2. Logical or(or)

# ## if op1 == True(1) then output == op1
# ## if op1 == False(0) then output == op2

# print(10 or 20)
# print(0 or 1)
# print('hello' or [])
# print(() or '')

# ## Logical not(not):

# ## if op == True then output == False
# ## if op == False then output == True
# print(not(10))
# print(not(' '))
# print(not(''))

# ##############################################################################

# ##3. Relational Operator/ Comparision Operator: it helps to compare two or more values
# ## it alwways retun boolean values

# ##1. equal to(==): it will return True if LHS and RHS both are exactly the same else wew get False

# print(1 == 1)
# print(1.1 == 1)
# print('hii' == 'hiiii')

# ##2. not equal(!=): it return TRue if RSH and LHS are differnet else it returns False

# print(1 != 1)
# print(1.1 != 1)
# print('hii' != 'hiiii')
# print('*****************************')

# ##3. Greater Than(>): it will return True if op1 > op2, it will return False if op1 < op2 or op1 == op2

# print(1 > 3)
# print(2.3 > 1.1)
# # print(2 + 6j > 4 + 9j)
# print(True > False)
# print('hello' > 'hiiii')
# print(ord('e'), ord('i'))
# print([1,2,3] > [1,2,3])
# print((11, 22, 33) > (111,22,4))
# print({1,2,3} > {4,5,6})
# print({7,2,3} > {4,5,6})
# print({7,2,3,4,5,6} > {4,5,6})
# print({1,2,3,4,5,6} > {4,5,6})    ## here it checks all the elements of set2 present in the set1 or not
# # print({12:3} > {13:5})

# ## col1                            col2
# # v1, v2,....                         val1, val2,................
# #
# # if v1 > val1  ===> True
# # if v1 < val1 ==> False
# # if v1 == val1 ==> then it checks for next values

# ## Greater Than or equal to(>=): it will return True if op1 > op2 or op1 == op2 else it return False
# ## less than (<): it will return True if op1 < op2, it will return False if op1 > op2 or op1 == op2

# print({7,2,3} < {4,5,6,7,2,3})   ## it will check all elements of set1 present in set2 or not

# ## less than or equal to(<=): it will return True if op1 < op2 or op1 == op2 else it return False


# #########################################################################################

# ##4. Assignment Operator: it helps to assign the values to variables

a = 10
b = 20
# a = a + b
# print(a)

# a += b
# print(a)

# a -= b
# print(a)

b *= a
print(b)
# print('****************************')

# ###########################################################################

# ##5. Membership Operator: it helps to check the values present in the collection or not

# ##1. in: it will return True if value present in the collection else it will return false
# ## syntax:   val in collections

# print(1 in [1,2,3])
# print('p' in 'python')
# print('py' in 'python')
# print('pn' in 'python')
# # print(1 in 1234)
# print(1 in {'a':1})
# print('a' in {'a':1})
# print('********************************')

# ##2. not in: it will return True if value not present in the collection else it will return false
# ## syntax:   val not in collections

# print(1 not in [1,2,3])
# print('p' not in 'python')
# print('py' not in 'python')
# print('pn' not in 'python')
# # print(1 not in 1234)
# print(1 not in {'a':1})
# print('a' not in {'a':1})
# print('********************************')

# #########################################################################################

# ##6. identity Operator: it checks two variables pointing to same address or not

# ##1. is: it will return True if two variables pointing to same address else it will return False
# ## syntax:  var1 is var2

# x = 100
# y = 300
# z = 100

# print(x is y)
# print(id(x), id(y), id(z))
# print(x is z)

# ##2. is not: it will return True if two variables are not pointing to same address else it will return False
# ## syntax:  var1 is not var2

# print(x is not z)
# print(y is not x)













