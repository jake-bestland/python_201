# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def features(**kwargs: int) -> str:   #this elims mypy error?
#def features(**kwargs: dict[str, int]) -> str:
    """ Lists Features and their amount.

    Args:
        **kwargs (dict[str, int]): a dictionary with a 'str' key and 'int' value.
        dict[str]: features of the listing that have a value. e.g. "Bedrooms", "Bathrooms", "Acres", or "Sq. ft."
        dict[int]: the amount of the features.

    Returns:
        str: an introductory sentence with a list of the features and their values formated nicely.
    """
    print(f"Here are some of the main features for this listing: \n")
    pros = ""
    for feat, amt in kwargs.items():
        sentence = f"* {feat}: {amt} \n"
        pros += sentence + "\n"

    return pros

feats = {"Bedrooms": 3, "Bathrooms": 2, "Acres": 2, "Sq. Ft.": 3500}

print(features(**feats))