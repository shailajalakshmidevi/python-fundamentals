# # 1.num = int(input("Enter a number: "))
# sq = num * num
# digit_sum = sum(int(d) for d in str(sq))

# if digit_sum == num:
#     print(num, "is a Neon Number")
# else:
#     print(num, "is not a Neon Number")


# 2

# students = [
#     {"name": "john", "grade": "A", "age": 26},
#     {"name": "jane", "grade": "B", "age": 28},
#     {"name": "dave", "grade": "B", "age": 22}
# ]

# students_sorted = sorted(students, key=lambda x: (x['age'], x['grade'], x['name']))
# print(students_sorted)



# 3

# portfolio = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]

# portfolio_sorted = sorted(portfolio, key=lambda x: (x['name'], x['shares'], x['price']))
# print(portfolio_sorted)




# 4

# string = "hello world welcome to python programming hi there"
# words = string.split()
# d = {}

# for w in words:
#     d.setdefault(w[0], []).append(w)

# print(d)



# 5

# with open("data.txt") as f:
#     ips = [line.strip() for line in f]

# print("All IPs:", ips)

# unique_ips = set(ips)
# print("Unique IPs:", unique_ips)

# freq = {ip: ips.count(ip) for ip in unique_ips}
# print("IP Frequency:", freq)




# 6


# def validate(func):
#     def wrapper(name):
#         if len(name) >= 5:
#             print("You have good name")
#         else:
#             print("Add few more characters")
#         return func(name)
#     return wrapper

# @validate
# def display(name):
#     print("Name is:", name)

# display("John")
# display("Krishna")




# 7

# string = 'work hard to get success'
# out = " ".join(word[::-1] for word in string.split())
# print(out)  



# 8

# students = [
#     ["John", "john@mail.com", "12345"],
#     ["Jane", "jane@mail.com", "67890"],
#     ["Dave", "dave@mail.com", "54321"]
# ]

# choice = int(input("Enter 1 for names, 2 for mails, 3 for ph_no: "))

# if choice == 1:
#     print([s[0] for s in students])
# elif choice == 2:
#     print([s[1] for s in students])
# elif choice == 3:
#     print([s[2] for s in students])
# else:
#     print("Invalid choice")




# 9

# words_to_num = {"one":1, "two":2, "three":3, "four":4, "five":5,
#                 "six":6, "seven":7, "eight":8, "nine":9, "zero":0}

# string = 'one eight three'
# out = sum(words_to_num[w] for w in string.split())
# print(out)   



# 10

# num_to_words = ["zero","one","two","three","four","five","six","seven","eight","nine"]

# number = 183
# out = " ".join(num_to_words[int(d)] for d in str(number))
# print(out)   


# 11

# tuples = [("Alice", 25), ("Bob", 30), ("Carol", 20), ("David", 25)]
# result = sorted(tuples, key=lambda x: (x[1], x[0]))
# print(result)



# 12

# list1 = [1, 2, 3, 4]
# list2 = [10, 20, 30, 40]

# result = list(map(lambda x, y: x*y, list1, list2))
# print(result)  



# 13

# strings = ["hello", "", "world", "", "python"]
# result = list(filter(None, strings))
# print(result)   



# 14

# words = ["apple", "banana", "cherry", "date"]
# result = [w.capitalize() for w in words]
# print(result)


# 15
# words = ["hello", "world", "python", "programming"]
# count_vowels = lambda w: sum(1 for c in w if c in "aeiou")

# result = list(map(count_vowels, words))
# print(result)  



# 16

# list_ = ['hai', 'take', 'care']
# result = {i: val for i, val in enumerate(list_)}
# print(result)  




# 17

# s = input("Enter string: ")
# if len(s) % 2 == 0:
#     print(s[::-1])
# else:
#     print(s)




























