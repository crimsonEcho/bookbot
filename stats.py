import sys

def get_book_text():
    with open(sys.argv[1]) as book:
        book_text = book.read()
        return book_text.split()

def book_string():
    with open(sys.argv[1]) as book:
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

def sort_on(items):
    return items["nums"]

def list_dicts():
    original_dict = book_characters()
    list_of_dicts = []

    for key in original_dict:
        new_dict = {}
        if key.isalpha():
            new_dict = {"chars":key,"nums":original_dict[key]}
            list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

def char_report():
    lines = []
    for item in list_dicts():
        lines.append(f"{item['chars']}: {item['nums']}")
    return "\n".join(lines)
