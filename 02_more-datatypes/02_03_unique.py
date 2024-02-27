# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]


a = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

b = []
for x in a:
    if a.count(x) <= 1:
        b.append(x)
print(b)

