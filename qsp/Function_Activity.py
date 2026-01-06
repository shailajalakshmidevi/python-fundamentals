
# Activity_on_Functions
#
# 1. WAP to check the given number is perfect number

## 4 ===> 1 + 2 ==> 3(not perfect)
## 6 ===> 1 + 2 + 3 ===> 6(perfect number)

def perfect(number):
    sum_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_divisors += divisor
    if number == sum_divisors:
        return 'the given number is perfect'
    else:
        return 'the given number is not perfect'
# print(perfect(6))


# 2. WAP to check the given number is amstrong number

# 123 ==> 1 ** 3 + 2 ** 3 + 3 ** 3 ==> 1 + 8 + 27(not amstrong)
# 153 ==> 1 ** 3 + 5 ** 3 + 3 ** 3 ===> 1 + 125 + 27(amstrong)

def amstrong(number):
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit) ** len(str(number))
    if number == sum_digit:
        return 'the given number is amstrong number'
    else:
        return 'the given number is not amstrong number'
# print(amstrong(4))


# 3. WAP to check the given number is strong number

## 123 ==> 1! + 2! + 3! ==> 1 + 2 + 6 ==>(not strong)
## 145 ==> 1! + 4! + 5 ! ==> 1 + 24 + 120==> 145(strong number)

def factorial(number):
    product = 1
    for num in range(1, number + 1):
        product *= num
    return product
# print(factorial(4))

def strong(number):
    sum_digit = 0
    for digit in str(number):
        sum_digit += factorial(int(digit))        ## factioral(1)
    if number == sum_digit:
        print('the given number is strong')
    else:
        print('the given number is not strong')
# strong(145)


# 4. Wap to check the given number is harshad number

# 123 ==> 1 + 2 +3 ==> 6(not harsad number)
## 81 ==> 1 + 8 ==> 9 (harshad number)

def harshad(number):
    sum_digit = 0
    for digit in str(number):
        sum_digit += int(digit)
    if number % sum_digit == 0:
        print('the given number is harshad')
    else:
        print('the given number is not harshad')
# harshad(81)

# 5. Given a list of integers, return True if the sequence of numbers 1, 2, 3 appears in the list somewhere.
# # For example:
# 	# listCheck([1, 1, 2, 3, 1]) → True
# 	# listCheck([1, 1, 2, 4, 1]) → False
# 	# listCheck([1, 1, 2, 1, 2, 3]) → True

def check_sequence(list_):
    for i in range(len(list_) - 2):
        if list_[i] == 1 and list_[i + 1] == 2 and list_[i + 2] == 3:
            return True
    return False
# print(check_sequence([1, 1, 2, 3, 1]))

# 6. Given a string, return a string where for every char in the original, there are two chars.
# 	# doubleChar('The') → 'TThhee'
# 	# doubleChar('AAbb') → 'AAAAbbbb'
# 	# doubleChar('Hi-There') → 'HHii--TThheerree'

def double_character(string):
    out = ''
    for char in string:
        out += char * 2
    print(out)
# double_character('The')

# 7. Wap to get the following output
# 	# dict_ = {'A':10, 'B':20, 'c':10, 'D':30, 'E':20}
# 	# output = {10:['A', 'C'], 20:['B', 'E'], 30:['C']}

def create_dict(dict_):
    out = {}
    for key, value in dict_.items():
        if value not in out:
            out[value] = [key]
        else:
            out[value] += [key]
    print(out)
# create_dict({'A':10, 'B':20, 'c':10, 'D':30, 'E':20})











