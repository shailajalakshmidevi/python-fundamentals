# 1
# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 3 == 0:
#     print("Divisible by both 2 and 3")
# else:
#     print("Not divisible by both")





# 2
# length = int(input("Enter length: "))
# breadth = int(input("Enter breadth: "))
# if length == breadth:
#     print("It is a square")
# else:
#     print("It is not a square")




# 3
# num = int(input("Enter a number: "))
# if num < 0:
#     print("Absolute value:", -num)
# else:
#     print("Absolute value:", num)





# 4
# year = int(input("Enter year: "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")









# 5
# num = input("Enter 4-digit number: ")
# if len(num) == 4:
#     print("Reversed:", num[::-1])
# else:
#     print("Not a 4-digit number")





# 6
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")





# 7
# a = int(input("Enter first: "))
# b = int(input("Enter second: "))
# c = int(input("Enter third: "))
# if a <= b and a <= c:
#     print("Smallest is", a)
# elif b <= a and b <= c:
#     print("Smallest is", b)
# else:
#     print("Smallest is", c)




# 8
# 


# 9
# age = int(input("Enter age: "))
# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")




# 10
# a = int(input("Enter side1: "))
# b = int(input("Enter side2: "))
# c = int(input("Enter side3: "))
# if a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")




# 11
lst1 = [eval(input("Enter first: "))]
lst2 = [eval(input("Enter last: "))]

if isinstance(lst1[0], str) and isinstance(lst2[-1], str):
    print("Both first and last are strings")
else:
    print("Not both are strings")


# 12
# percent = float(input("Enter percentage: "))
# if percent >= 75:
#     print("Distinction")
# elif percent >= 60:
#     print("First class")
# elif percent >= 35:
#     print("Second class")
# else:
#     print("Fail")



# 13

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# t = (a, b)

# if t[0] % 2 == 0:
#     print("First element is even")
# else:
#     print("First element is odd")


# 14
# a = int(input("Enter first: "))
# b = int(input("Enter second: "))
# c = int(input("Enter third: "))
# if a < b and a < c:
#     print("Smallest:", a)
# elif b < c:
#     print("Smallest:", b)
# else:
#     print("Smallest:", c)



# 15
# a = 56
# if a == 10:
#     print("Hello")
# else:
#     print("Good Bye")  
    # good bye



# 16
# length = 5
# breadth = 10
# Area = length * breadth
# Perimeter = 2 * (length + breadth)
# if Area > Perimeter:
#     print("Area of the rectangle is greater than the Perimeter of the rectangle")
# else:
#     print("Perimeter of the rectangle is greater than the Area of the rectangle")
    

#     # Area of the rectangle is greater than the Perimeter of the rectangle")


# 17
# a = "I am a Data Scientist"
# if "Data" in a:
#     print("It is present")
# else:
#     print(False)

# It is present




# 18

# first = 25
# second = 34
# third = 45
# if first >= second and first >= third:
#     print(first)
# elif second >= first and second >= third:
#     print(second)
# elif third >= first and third >= second:
#     print(third)
# else:
#     print("All of the values are equal")

# 45





# 19
# num = int(input("Enter a number: "))
# if num % 10 == 5:
#     print("Last digit is 5")
# else:
#     print("Last digit is not 5")





# 20
# ch = input("Enter a character: ")
# if not ch.isalnum():
#     print("Special character")
# else:
#     print("Not a special character")









# 21
# a = eval(input("Enter first: "))
# b = eval(input("Enter second: "))
# t=(a,b)
# if type(t[0]) == type(t[1]):
#   print("Tuple is homogenous")
# else:
#    print("Tuple is not homogenous")




# 22
# ch = input("Enter a character: ")
# if ch.isupper():
#     print(ch.lower())
# elif ch.islower():
#     print(ch.upper())
# elif ch.isdigit():
#     print(int(ch) % 3)
# else:
#     print("ASCII:", ord(ch))



