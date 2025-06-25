from stats import count_the_words, count_the_characters, sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    words = count_the_words(file_contents)
    char_count = count_the_characters(file_contents)
    character_sorted = sort_characters(char_count)
    return words, char_count, character_sorted

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    word_count, character_count, character_sorted = get_book_text(path)
    print(f"{word_count} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for entry in character_sorted:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")
main()
