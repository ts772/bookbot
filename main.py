
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import word_count
from stats import character_count
from stats import report
filepath = sys.argv[1]

word_count = word_count(filepath)

character_count = character_count(filepath)
#print(character_count)

report = report(filepath)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")
for dic in report:
    for key, value in dic.items():
        if key.isalpha() == True:
            print(f"{key}: {value}")

    
