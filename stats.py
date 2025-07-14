def get_book_text():
    with open("books/frankenstein.txt") as my_file:
        book = my_file.read()
        return book

def book_string():
    x = get_book_text()
    return x.split(None)

def book_characters():
    y = get_book_text()
    return y.lower()

book_characters()