from analyser import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <filename>")
    exit()

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        text = file.read()
except FileNotFoundError:
    print("Error: File not found")
    exit()


print("Text:", text)

(vowel_count, consonant_count, vowel_list, consonant_list,
 char_count, total_chars, words, words_length) = analyser(text)

print("\nTotal vowels =", vowel_count)
print("Vowels are =", vowel_list)

print("\nTotal consonants =", consonant_count)
print("Consonants are =", consonant_list)

print("\nTotal characters =", total_chars)

print("\nWords in text =", words)
print("Total words =", words_length)

print("\nCharacter frequency =", char_count)