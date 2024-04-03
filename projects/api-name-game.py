# Add an API call to your CLI game that assigns a name to your player.
import requests

user_name_len = 0
while not (user_name_len >= 2 and user_name_len <= 40):
    name = input("What is your name?: ")
    user_name_len = len(name)
    
un_url = f"https://uzby.com/api.php?min={user_name_len}&max={user_name_len}"
user_game_name = requests.get(un_url).text