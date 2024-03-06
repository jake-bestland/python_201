# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.


from pathlib import Path

word_path = Path("/Users/jakebestland/Documents/codingnomads/python-201-main/03_file-input-output/words.txt")

short = 100
short_word = []
long = 0
long_word = []
w_count = []
with word_path.open() as word_file:
    for w in word_file:
        w = w.strip()
        if len(w) < short:
            short = len(w)
            short_word.clear()
            short_word.append(w)
        elif len(w) == short:
            short_word.append(w)
        
        if len(w) > long:
            long = len(w)
            long_word.clear()
            long_word.append(w)
        elif len(w) == long:
            long_word.append(w)
        
        w_count.append(w)
print(short_word)
print(long_word)
print(len(w_count))