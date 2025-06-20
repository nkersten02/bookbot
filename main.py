import sys
def get_book_text(file):
    with open(file) as f:
        contents = f.read()
    return contents

from stats import word_count
from stats import char_count
from stats import sort_on
from stats import sorter

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    words = word_count(get_book_text(sys.argv[1]))
    character_count = char_count(get_book_text(sys.argv[1]))
    final_count = sorter(character_count)
    print("============= BOOKBOT =================")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("------------ Word Count ---------------")
    print(f"Found {words} total words")
    print("---------- Character Count ----------------")
    for entry in final_count:
        if entry["name"].isalpha():
            print(f"{entry["name"]}: {entry["num"]}")
    return

main()