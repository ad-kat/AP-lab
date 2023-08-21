def count_upper_lower_case(string):
  """
  Counts the number of upper case and lower case letters in a string.

  Args:
    string: The string to be counted.

  Returns:
    A tuple of the number of upper case letters and the number of lower case letters.
  """
  upper_case_count = 0
  lower_case_count = 0
  for letter in string:
    if letter.isupper():
      upper_case_count += 1
    elif letter.islower():
      lower_case_count += 1
  return upper_case_count, lower_case_count


string = "The quick Brown Fox"
upper_case_count, lower_case_count = count_upper_lower_case(string)
print("no. of uppercase characters:", upper_case_count)
print("no. of lowercase characters:", lower_case_count)
