def count_the_words(book_string):
    number_of_words = len(book_string.split())
    return number_of_words

def count_the_characters(book_string):
    lower_book = book_string.lower()
    characters = {}
    for character in lower_book:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters