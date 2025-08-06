def get_book_text():
    with open("books/frankenstein.txt") as book:
        book_text = book.read()
        return book_text.split()

def book_string():
    with open("books/frankenstein.txt") as book:
        words = book.read()
        return words.lower()

def book_characters():
    count = {}
    for letter in book_string():
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count

book_characters()