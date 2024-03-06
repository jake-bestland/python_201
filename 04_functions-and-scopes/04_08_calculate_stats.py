# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.
from statistics import mean

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(list_of_num):
  # define the function here
  """Takes a list of numbers and finds the maximum, minimum, average and sum of the numbers. 

  Args:
      list_of_num (list): A list of numbers

  Returns:
      str: a string displaying the maximum, minimum, average and sum of the numbers.
  """
  max_num = max(list_of_num)
  min_num = min(list_of_num)
  avg = mean(list_of_num)
  list_sum = sum(list_of_num)
  return f"maximum = {max_num}, minimum = {min_num}, average = {avg}, sum = {list_sum}"

# call the function below here
print(stats(example_list))