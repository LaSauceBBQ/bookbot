from stats import get_num_words, get_nb_char, sort_list
import sys



def get_book_text(path:str):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------\nFound {get_num_words(path)} total words\n--------- Character Count -------")
    items = sort_list(get_nb_char(path))
    for item in items:
        if item["char"].isalpha() == False:
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
    