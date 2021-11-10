"""Count words in file."""

import sys

input_file = open(sys.argv[1])

word_counts = {}

for line in input_file:
    # Remove trailing whitespace at the end of each line
    line = line.rstrip()

    # Split the line by spaces to get a list of words
    words = line.split()

    for word in words:
        # Set the word count to whatever it was + 1; if it wasn't found at all,
        # we'll use `.get(word, 0)` to return 0 if the word wasn't already in
        # the dictionary
        word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(word, count)
