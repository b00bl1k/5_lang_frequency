import string
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as fh:
        return fh.read()


def split_text_by_words(text):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    without_punctuation = text.translate(table)
    return without_punctuation.lower().split()


def get_most_frequent_words(text):
    words = split_text_by_words(text)
    freq_dict = {}
    for word in words:
        if word in freq_dict.keys():
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    top_words = sorted(freq_dict.items(), key=lambda kv: kv[1], reverse=True)
    return top_words[:10]


def main():
    try:
        result = load_data(sys.argv[1])
        words = get_most_frequent_words(result)
        print("Most frequent words in text:")
        for word in words:
            print(" {}:{}".format(*word))
    except FileNotFoundError:
        sys.exit("File not found")
    except IndexError:
        sys.exit("Invalid command line arguments")


if __name__ == "__main__":
    main()
