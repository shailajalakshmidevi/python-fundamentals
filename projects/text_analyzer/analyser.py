def analyser(text):
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
        
  
    return vowel_count,consonant_count,vowel_list,consonant_list,char_count,total_chars,words,words_length
    