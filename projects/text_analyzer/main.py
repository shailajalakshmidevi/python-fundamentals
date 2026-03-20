text = "hello world"

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

vowel_list = []
consonant_list = []
char_count = {}

for char in text:
    if char not in char_count:
        char_count[char] = 1
    else:
        char_count[char] += 1   
    if char in vowels:
        vowel_count += 1
        vowel_list.append(char)
    elif char.isalpha():
        consonant_count += 1
        consonant_list.append(char)
  

total_chars = len(text)

words = text.split()
words_length = len(words)

print("Total vowels =", vowel_count)
print("Vowels are =", vowel_list)

print("Total consonants =", consonant_count)
print("Consonants are =", consonant_list)

print("Total characters =", total_chars)

print("Words in text =", words)
print("total words =", len(words))
print("character frequency=",char_count)