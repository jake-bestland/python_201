# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


text = input("Please write something here: ")
words = text.split()

result_list = [tuple(x) for x in words]
print(result_list)