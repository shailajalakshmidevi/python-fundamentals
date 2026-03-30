from analyser import *
import sys

if len(sys.argv) <2:
    
     print("error")
     exit()
else:    

     filename = sys.argv[1]
     with open("sample.txt") as file:
          text = file.read()
     print("Text:", text)
     print(filename)


vowel_count, consonant_count, vowel_list, consonant_list, char_count, total_chars, words, words_length = analyser(text)

print("Total vowels =", vowel_count)
print("Vowels are =", vowel_list)

print("Total consonants =", consonant_count)
print("Consonants are =", consonant_list)

print("Total characters =", total_chars)

print("Words in text =", words)
print("Total words =", words_length)

print("Character frequency =", char_count)