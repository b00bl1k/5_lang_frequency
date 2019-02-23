from collections import Counter
import string
import sys


DISPLAY_WORDS_COUNT = 10


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as fh:
        return fh.read()


def split_text_by_words(text):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    without_punctuation = text.translate(table)
    return without_punctuation.lower().split()


def get_most_frequent_words(text):
    words = split_text_by_words(text)
    return Counter(words).most_common(DISPLAY_WORDS_COUNT)


def main():
    try:
        text = load_data(sys.argv[1])
        words = get_most_frequent_words(text)
        print("Most frequent words in text:")
        for word in words:
            print(" {}:{}".format(*word))
    except FileNotFoundError:
        sys.exit("File not found")
    except IndexError:
        sys.exit("Invalid command line arguments")


if __name__ == "__main__":
    main()
