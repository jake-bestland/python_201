# Write a function called `make_sandwich()` that sticks to the following:
# - takes a type of bread as its first, required argument
# - takes an arbitrary amount of toppings
# - returns a string representing a sandwich with the bread on top
#   and bottom, and the toppings in between.

def make_sandwich(bread, *toppings):
    """generates a list of ingredients desired to make a sandwich.

    Args:
        bread (str): the bread to use for the top and bottom of sandwich, e.g., "wheat"
        toppings (str): the ingredients to be put into the sandwich

    Returns:
        str: a sandwich with the bread on top
#   and bottom, and the toppings in between.
    """
    top_list = ""
    for ingredients in toppings:
        top_list += f"{ingredients}, "
    sandwich = f"{bread} bread, {top_list}{bread} bread"
    return sandwich

print(make_sandwich("wheat", "mayo", "mustard", "cheese", "ham", "lettuce", "tomatoe", "pickle"))
    