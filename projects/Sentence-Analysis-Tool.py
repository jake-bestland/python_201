# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!
# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28
import string


user_input = input("Please write a sentence.: ")

low_case = []
up_case = []
punc = []
tot_char = []

for char in user_input:
    tot_char.append(char)
    if char.isupper():
        up_case.append(char)
    if char.islower():
        low_case.append(char)
    if char.isspace():
        tot_char.remove(char)
    if char in string.punctuation:
        punc.append(char)

char_dict = {}
char_dict['Lower case'] = len(low_case)
char_dict['Upper case'] = len(up_case)
char_dict['Punctuatiom'] = len(punc)
char_dict['Total chars'] = len(tot_char)

for k, v in char_dict.items():
    print(f"{k}: {v}")
