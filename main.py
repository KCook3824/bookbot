from stats import count_the_words, count_the_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = count_the_words(file_contents)
    char_count = count_the_characters(file_contents)
    return words, char_count

def main():
    word_count, character_count = get_book_text("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(character_count)

main()
