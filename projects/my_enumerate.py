# Reproduce the functionality of Python's built-in `enumerate()` function.
# Define a function called `my_enumerate()` that takes an iterable as input
# and gives back both the element as well as its index position as an integer.

def my_enumerate(iterable, start=0):  # add your arguments
      # add your code implementation
      n = start
      for elem in iterable:
            yield n, elem
            n += 1


months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# print(list(my_enumerate(months, 1)))
for index, months in my_enumerate(months, 1):
    print(f"{index}: {months}")