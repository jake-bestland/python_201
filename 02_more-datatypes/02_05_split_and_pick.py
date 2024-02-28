# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

string = input("Please write something here: ")


words = string.split()
print(words)


num_w = {w: words.count(w) for w in words}
print(num_w)
print(max(num_w.values()))

most = 0
most_common = ""
for w in num_w:
    num_w.get(w)
    if num_w.get(w) > most:
        most = num_w.get(w)
        most_common = w
    
print(most_common)