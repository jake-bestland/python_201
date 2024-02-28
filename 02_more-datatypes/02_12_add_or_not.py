# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

points = 11
lives = 5
numbers = set()
print("Welcome to my memory game!  To win the game, enter enough new numbers without any repeats.  Enter too many duplicate numbers and you will lose!")
while True:
    if lives == 0:
        print("I'm sorry, you are out of lives.  You lose!")
        break
    if points == 0:
        print("Congratulations, You win!")
        break
    
    user_input = (input("Please enter a number: "))
    
    if not user_input.isdigit():
        print("I'm sorry, that isn't a number.  Try again.")
        continue
    elif user_input in numbers:
        print(f"You have already entered that number!  Try again with a new number, you have {lives} lives remaining!")
        lives -= 1
        continue
    else:
        numbers.update(user_input)
        print(f"Good job! you have not entered that number yet!  You need {points} more points until you win!")
        points -= 1
        continue


