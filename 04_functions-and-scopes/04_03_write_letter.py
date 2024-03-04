# Define a function called `write_letter()` that takes as input a `name`
# and a `text` argument. In the body of the function, create a greeting
# message with the `name` input, as well as a goodbye message that uses
# the `name` again. Combine that with the input `text` to return a
# complete `letter`.


def write_letter(name, text):
    greeting = f"Hello {name}! How are you?"
    goodbye =  f"Goodbye {name}! I hope to talk to you again soon!"
    message = f"{text}"
    letter = f"{greeting} {message} {goodbye}"
    return letter

print(write_letter("Jake", "We should go to a hockey game next weekend!"))