def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_char_count(text)
    sorted_chars = sort_alphabet(num_chars)
    print_report(sorted_chars, num_words)

def sort_on(dict):
    return dict['num']

def sort_alphabet(text):
    new_alphabet = []
    for letter,count in text.items():
        new_alphabet.append({'name': letter, 'num': count})
    new_alphabet.sort(reverse=True, key=sort_on)
    return new_alphabet

def print_report(sorted_chars, num_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    for char in sorted_chars:
        print(f"The '{char}' character was found {char['num']} times.")
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    alphabet = {}
    for char in range(ord('a'), ord('z') + 1):
        alphabet[chr(char)] = 0
    for char in text.lower():
        if char in alphabet:
            alphabet[char] += 1
    return alphabet

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()