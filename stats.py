def get_book_text(fpath):
    with open(fpath) as f:
        file_contents = f.read()
        # print(file_contents)
        return file_contents

def get_text_words(book_string):
    book_wc = len(book_string.split())
    return book_wc

def get_text_letters(book_string):
    return_dict = {}
    # get words in a list
    book_words = book_string.split()
    # join words together without whitespaces
    book_letters = "".join(book_words)
    
    # Allocate all letters into a dictionary
    for letter in book_letters:
        # lowercase everything
        letter = letter.lower()
        if not letter.isalpha():
           continue 
        if letter in return_dict:
            return_dict[letter] += 1
        else:
            return_dict[letter] = 1
    
    return return_dict
