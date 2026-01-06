
## syntax:

# for variable in collections:
#     for var in variable:
#         TSB

## WAP TO GET THE FOLLOWING OUTPUT
list_ = ['hello', 'hai', 'good', 'morning']
# out = ['eo', 'ai', 'oo', 'oi']

out = []
for string in list_:
    vowel = ''
    for char in string:
        if char in 'aeiouAEIOU':
            vowel += char
    out.append(vowel)
# print(out)

## WAP TO GET THE FOLLOWING OUTPUT
LIST_ = [123, 32, 31, 21]
# OUT = [6, 5, 4, 3]
out = []
for num in LIST_:
    sum_digit = 0
    for digit in str(num):     ## '123'
        sum_digit += int(digit)
    out.append(sum_digit)
print(out)

## WAP TO GET THE FOLLOWING OUTPUT
list_ = [12, 5.6,'hello', 3, 'abc']
# out = {12:144, 'hello':'h104e101l1o8l1o8o111', 3:9, 'abc':'a97b98c99'}

out = {}
for element in list_:
    if type(element) == int:
        out[element] = element ** 2
    elif type(element) == str:
        char_ascii = ''
        for char in element:
            char_ascii += char + str(ord(char))
        out[element] = char_ascii
print(out)

# '' + 'h' + '104' ==> 'h104'
# 'h104' + 'e' + '101' ==> 'h104e101'

# Wap to get the following output.
In=['hello',227,3.4,'last',189,34]
# Out=[722,981,43]

## WAP TO GET THE FOLLOWING OUTPUT
LIST_ = ['hAi', 'HEllO', 'GOod']
# out: ['A', 'HEO', 'GO']







