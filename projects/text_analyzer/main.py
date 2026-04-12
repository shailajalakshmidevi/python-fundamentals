import sys
import logging
from analyser import analyser
# 🔹 Logging setup
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


if len(sys.argv) < 2:
    print("Usage: python3 main.py <filename>")
    logging.warning("No filename provided")
    exit()

filename = sys.argv[1]

try:
    logging.info(f"Opening file: {filename}")

    with open(filename, "r") as file:
        text = file.read()

    print("Text:", text)
    logging.info("File read successfully")

    v_count, c_count, v_list, c_list, freq, total_chars, words, total_words = analyser(text)
    print("\nTotal vowels =", v_count)
    print("Vowels =", v_list)

    print("\nTotal consonants =", c_count)
    print("Consonants =", c_list)

    print("\nTotal words =", total_words)
    print("Words =", words)

    print("\nCharacter frequency =", freq)

    logging.info("Analysis completed successfully")

except FileNotFoundError:
    print("Error: File not found")
    logging.error(f"File not found: {filename}")