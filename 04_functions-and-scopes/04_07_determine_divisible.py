# Write a script where you complete the following tasks:
# - define a function that determines whether the number is
#   divisible by 4 OR 7 and returns a boolean
# - define a function that determines whether a number is
#   divisible by both 4 AND 7 and returns a boolean
# - take in a number from the user between 1 and 1,000,000,000
# - call your functions, passing in the user input as the arguments,
#   and set their output equal to new variables 
# - print your the result variables with descriptive messages

def div_4_or_7(number):
    """Check if a number is divisible by either 4 or 7.

    Args:
        number (int): the number you want to check if it is divisible by 4 or 7

    Returns:
        bool: a true or false value
    """
    return number % 4 == 0 or number % 7 ==0
    

def div_both_4_7(number):
    """check if a number is divisible by both 4 and 7.

    Args:
        number (int): the number you want to check if it is divisible by both 4 and 7

    Returns:
        bool: a true or false value
    """
    return number % 4 == 0 and number % 7 == 0
    

while True:
    user_num = input("Select a number between 1 and 1,000,000,000: ")
    if not user_num.isdigit():
        print("Sorry, that is not a number. Please enter a number.")
        continue
    number = int(user_num)
    if number < 1 or number > 1000000000:
        print("Sorry, that number is out side the range. Please pick a number in the range.")
        continue
    if number >= 1 and number <= 1000000000:
        if div_4_or_7(number) == True:
            answer1 = "is"
        else:
            answer1 = "is not"
        if div_both_4_7(number) == True:
            answer_both = "is"
        else:
            answer_both = "is not"
        break

print(f"The number you have selected {answer1} divisible by EITHER 4 OR 7!")
print(f"The number you have selected {answer_both} divisible by BOTH 4 AND 7!")