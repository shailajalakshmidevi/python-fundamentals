import sys
import logging
from analyser import analyser

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if len(sys.argv) < 2:
    print("Usage: python3 main.py <file1>,<file2> ....")
    logging.warning("No filename provided")
    exit()

for filename in sys.argv[1:]:

    try:
        logging.info(f"Opening file: {filename}")

        with open(filename, "r") as file:
             text = file.read()
        print(f"\n    File: {filename}")

        print("Text:", text)
        

        v_count, c_count, v_list, c_list, freq, total_chars, words, total_words = analyser(text)
        print("\nTotal vowels =", v_count)
        print("Vowels =", v_list)

        print("\nTotal consonants =", c_count)
        print("Consonants =", c_list)

        print("\nTotal words =", total_words)
        print("Words =", words)

        print("\nCharacter frequency =", freq)

        logging.info(f"File read successfully:{filename}")
    except FileNotFoundError:
        print("Error: File not found")
        logging.error(f"File not found: {filename}")