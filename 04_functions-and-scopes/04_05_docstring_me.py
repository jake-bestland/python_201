# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    #"""Add your docstring here."""
    """converts kilometers into miles.

    Args:
        km (int): the distance in kilometers to be converted into miles

    Returns:
        miles (int): the distance in miles
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
