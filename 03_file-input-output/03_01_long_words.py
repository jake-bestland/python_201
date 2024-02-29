# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

word_path = Path("/Users/jakebestland/Documents/codingnomads/python-201-main/03_file-input-output/words.txt")

with word_path.open() as word_file:
    #print(word_file.read())

    long_words = []
    for w in word_file:
        w = w.rstrip()
        if len(w) > 20:
            long_words.append(w)

    print("\n".join(long_words))