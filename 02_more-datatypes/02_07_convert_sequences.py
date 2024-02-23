# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"


tup = tuple([string])
print(tup)

list_str = list(tup)
print(list_str)

list_str = [string.replace('c', 'k')]
print(list_str)

tup2 = tuple(list_str)
print(tup2)