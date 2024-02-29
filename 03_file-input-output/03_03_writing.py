# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


from pathlib import Path

word_path = Path("/Users/jakebestland/Documents/codingnomads/python-201-main/03_file-input-output/words.txt")


w_list = []
with word_path.open() as word_file:
    for w in word_file:
        w = w.strip()
        w_list.append(w)

w_list.reverse()
print("\n".join(w_list))

with open("words_reverse.txt", "w") as r_list:
     r_list.write("\n".join(w_list))