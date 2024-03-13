# Using a list comprehension, create a *cartesian product* (google this!)
# of the given lists. Then open up your online shop ;)

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

cart = [(x, y) for x in colors for y in sizes]
print(cart)


# different formatting#

# c1 = [(colors[0], y) for y in sizes]
# c2 = [(colors[1], y) for y in sizes]
# print(f"{c1}\n{c2}")
