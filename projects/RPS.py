#rock, paper, scissors
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner

import random

def get_hand(hand):
    """takes user input 0-2 and prints rock, paper, or scissors.

    Args:
        hand (int): a number between 0-2

    Returns:
        str: the string eitherm, rock, paper or scissors.
    """
    hand_dict = {0: "Rock", 1: "Paper", 2: "Scissors"}
    return hand_dict[hand]

def determine_winner(player_hand, comp_hand):
    """determines who wins in rock paper scissors.

    Args:
        player_hand (int): a number between 0-2
        comp_hand (int): a number between 0-2

    Returns:
        str: the winner of the game.
    """
    if player_hand == comp_hand:
        return f"It's a draw!"
    if player_hand == 0:
        if comp_hand == 1:
            return f"Comupter wins! \nPaper covers Rock!"
        else:
            return f"You win! \nRock smashes Scissors!"
    if player_hand == 1:
        if comp_hand == 0:
            return f"You win! \nPaper covers Rock!"
        else:
            return f"Computer wins! \nScissors cut Paper!"
    if player_hand == 2:
        if comp_hand == 0:
            return f"Computer wins! \nRock smashes Scissors!"
        else:
            return f"You win! \nScissors cut Paper"


while True:
    player_input = input("Enter a number between 0-2 to choose rock, paper or scissors. (rock = 0. paper = 1 and scissors = 2) : ")
    
    if not player_input.isdigit():
        print("Sorry, this is not a valid input.  Please try again!")
        continue
    
    player_num = int(player_input)
    comp_num = random.randint(0, 2)
    
    if player_num < 0 or player_num > 2:
        print("Sorry this is not a valid number.  Please try again!")
        continue
    
    player_hand = get_hand(player_num)
    comp_hand = get_hand(comp_num)
    
    if player_num >= 0 and player_num <= 2:
        print(f"You chose, {player_hand}.")
        print(f"The computer chose, {comp_hand}.")
        print(determine_winner(player_num, comp_num))
        break
