# 5
# . WAP to check the given number is perfect number
# 2. WAP to check the given number is amstrong number
# 3. WAP to check the given number is strong number
# 4. Wap to check the given number is harsad number
# 5. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
# # For example:
# 	# listCheck([1, 1, 2, 3, 1]) → True
# 	# listCheck([1, 1, 2, 4, 1]) → False
# 	# listCheck([1, 1, 2, 1, 2, 3]) → True

# 6. Given a string, return a string where for every char in the original, there are two chars.
# 	# doubleChar('The') → 'TThhee'
# 	# doubleChar('AAbb') → 'AAAAbbbb'
# 	# doubleChar('Hi-There') → 'HHii--TThheerree'

# 7. Wap to get the following output
# 	# dict_ = {'A':10, 'B':20, 'c':10, 'D':30, 'E':20}
# 	# output = {10:['A', 'C'], 20:['B', 'E'], 30:['C']} 
# 8. WAP TO FIND THE SUM OF ASCII VALUE OF ALL THE SPECIAL CHARACTER PRESENT IN THE STRING
# 9. WAP TO FIND THE SUM OF ALL THE INDIVIDUAL DIGITS PRESENT IN THE GIVEN INTEGER NUMBER ONLY IF THE DIGIT IS EVEN
# 10.WAP get the sum of all the even digits we have the input string
# 11.WAP to extract all the string from the tuple only if the length of string > 4
# 12.WAP to extract all the int number from the list, if number having exactly 3digits
# 13. Give examples for each
# 	1. local variable 
# 	2. Global variable
# 	3. What is global keyword, give an example
# 	4. What is non-local keyword, give an example
# 	5. Tuple Packing
# 	6. Dictionary Packing
# 	7. Variable argument
# 	8. Unpacking 



# 5
def listCheck(lst):
    for i in range(len(lst)-2):
        if lst[i] == 1 and lst[i+1] == 2 and lst[i+2] == 3:
            return True
    return False

# print(listCheck([1,1,2,3,1]))   
# print(listCheck([1,1,2,4,1]))   
# print(listCheck([1,1,2,1,2,3])) 



# 6

def doubleChar(s):
    result = ""
    for ch in s:
        result += ch*2
    return result

# print(doubleChar("The"))       # TThhee
# print(doubleChar("AAbb"))      # AAAAbbbb
# print(doubleChar("Hi-There"))  # HHii--TThheerree


# 7
dict_ = {'A':10, 'B':20, 'C':10, 'D':30, 'E':20}
output = {}
for k, v in dict_.items():
    output.setdefault(v, []).append(k)
# print(output)
    

    #8
     
s = input("Enter string: ")
total = 0
for ch in s:
    if not ch.isalnum() and not ch.isspace(): 
        total += ord(ch)
print("Sum of ASCII of special chars =", total)

# 9
# # num = int(input("Enter number: "))
# s = 0
# for d in str(num):
#     d = int(d)
#     if d % 2 == 0:
#         s += d
# # print("Sum of even digits =", s)
        

# 10
        
s = input("Enter string: ")
total = 0
for ch in s:
    if ch.isdigit() and int(ch) % 2 == 0:
        total += int(ch)
# print("Sum of even digits in string =", total)


# 11

t = ("apple", "cat", "banana", "dog", "orange")
result = [x for x in t if isinstance(x, str) and len(x) > 4]
# print(result) 
       


# 12

lst = [12, 345, 678, 90, 1001, 999]
result = [x for x in lst if isinstance(x, int) and 100 <= x <= 999]
print(result) 


# 13
# local
def fun():
    x = 10   # local
    print("Local x:", x)
fun()

# global variable
x = 50
def fun():
    print("Global x:", x)
fun()

# global keyword

x = 10
def fun():
    global x
    x = 20
fun()
print("x after global:", x)  

# nonlocal keywrd
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner changed"
    inner()
    print(x)
outer()

# tuple packing
t = 1, 2, 3, "hello"
print(t)

# dict packing
def fun(**kwargs):
    print(kwargs)

fun(a=10, b=20, c=30)

# var arg

def add(*args):
    return sum(args)

print(add(1,2,3,4))  

# unpacking
lst = [1,2,3]
a,b,c = lst
print(a,b,c)   




# 1
# num = int(input("Enter number: "))
# s = 0
# for i in range(1, num):
#     if num % i == 0:
#         s += i
# if s == num:
# #     print(num, "is a Perfect number")
# # else:
#     print(num, "is not a Perfect number")


# 2
    
# num = int(input("Enter number: "))
# n = len(str(num))
# s = 0
# for d in str(num):
#     s += int(d) ** n
# if s == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")



# 3

# import math
# num = int(input("Enter number: "))
# s = 0
# for d in str(num):
#     s += math.factorial(int(d))
# if s == num:
#     print(num, "is a Strong number")
# else:
#     print(num, "is not a Strong number")



# 4

num = int(input("Enter number: "))
s = sum(int(d) for d in str(num))
if num % s == 0:
    print(num, "is a Harshad number")
else:
    print(num, "is not a Harshad number")



    

















