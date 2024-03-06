# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

from pathlib import Path

word_path = Path("/Users/jakebestland/Documents/codingnomads/python-201-main/03_file-input-output/words.txt")

with word_path.open() as word_file:
    for w in word_file:
        w = w.strip()
        if len(w) > 20:
            print(w)
