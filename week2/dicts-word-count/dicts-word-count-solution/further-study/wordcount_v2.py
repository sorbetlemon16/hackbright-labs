"""Count words in file."""

import sys


def tokenize(filename):
    """Return list of words from file"""

    tokens = []

    with open(filename) as input_file:
        for line in input_file:
            # Remove trailing whitespace at the end of each line
            line = line.rstrip()

            # Split the line by spaces to get a list of words
            words = line.split()
            # add the words to our list of tokens
            tokens.extend(words)

    return tokens


def count_words(words):
    """Return dictionary of {word: count} from list"""

    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def print_words(word_counts):
    """Print words: count from dictionary"""

    for word, count in word_counts.items():
        print(word, count)


def normalize_words(words):
    """Return list of normalized words.

    Words are normalized by removing punctuation and converting letters
    so they're all lowercased.
    """

    normalized = []
    for word in words:
        no_punct = ""

        # Re-create `word` without punctuation
        for char in word:
            if char.isalpha():
                no_punct += char

        # Append lowercased version of `no_punct`
        normalized.append(no_punct.lower())

    return normalized


filename = sys.argv[1]
tokens = tokenize(filename)
tokens = normalize_words(tokens)
word_counts = count_words(tokens)
print_words(word_counts)
