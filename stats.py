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

def sort_on(items):
    return items["num"]

def sort_characters(character_dict):
    new_structure = []
    for character in character_dict:
        if character.isalpha() == True:
            dict_entry = {"char": character, "num": int(character_dict[character])}
            new_structure.append(dict_entry)
    new_structure.sort(reverse=True, key=sort_on)
    return new_structure