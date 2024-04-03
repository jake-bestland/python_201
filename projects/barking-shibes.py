# Use a quotes API, e.g. https://api.quotable.io/quotes/random
# to fetch a random quote. Then use string manipulation to convert it to
# Doge speech (https://en.wikipedia.org/wiki/Doge_(meme))
# Create a tiny webpage that displays a doge image together
# with the altered quote. You can get an image URL from another API:
# http://shibe.online/api/shibes
# Write the code logic to make the API calls and assign the output to
# `doged_quote` and `doge_image_url` respectively.
# Then write the `html` string to a `.html` file and look at it in your browser.
from pathlib import Path
import requests

quote_url = "https://api.quotable.io/quotes/random"
quote = requests.get(quote_url).json()[0]["content"]

doged_quote = f"Wow. {quote.upper()}. Much wisdom."


doge_img_url = "http://shibe.online/api/shibes"
doge_img = requests.get(doge_img_url).json()[0]


html = f"<p style='font-family:Comic Sans'>{doged_quote}</p><img src='{doge_img}'>"

file = Path().home().joinpath("Desktop").joinpath("doge.html")
file.write_text(html)