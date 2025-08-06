from stats import get_book_text
from stats import book_characters

def main():
    word_list = get_book_text()
    word_count = len(word_list)
    char_count = book_characters()
    print(f"{word_count} words found in the document.")
    print(char_count)
            
main()

