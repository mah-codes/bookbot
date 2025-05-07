import sys
from stats import get_book_text, get_text_words, get_text_letters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relative_path = sys.argv[1]
    
    book_text = get_book_text(relative_path)
    book_wc = get_text_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wc} total words")
    print("--------- Character Count -------")

    letters_dict = get_text_letters(book_text)
    letters_sorted_list = sorted(letters_dict, key=lambda letter:-letters_dict[letter])
    for letter in letters_sorted_list:
        print(f"{letter}: {letters_dict[letter]}")

main()
