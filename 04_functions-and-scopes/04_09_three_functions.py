# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.

# seasons_list = list(input("What are the four seasons? ").split())
# for index, season in enumerate(seasons_list):
#     print(f"{index}: {season}")



def greet(greeting: str, name: str) -> str:
    """Generates a greeting."""
    sentence = f"{greeting}, {name.capitalize()}!"
    return sentence

def sarcasm(text):
    result = ""
    for char in range(len(text)):
        if not char % 2:
            result = result + text[char].upper()
        else:
            result = result + text[char].lower()
    return result

def angry(text):
    sentence = ""
    for word in text.split():
        sentence += word.upper()
    return sentence



name = input("What is your first name? ")

intro = greet("Hello", name)
print(intro)
silly = sarcasm(intro)
print(silly)
yell = angry(silly)
print(yell)


