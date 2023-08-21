def union(list1, list2):
  """
  Finds the union of two lists.

  Args:
    list1: The first list.
    list2: The second list.

  Returns:
    A list containing all the elements of list1 and list2, without duplicates.
  """
  union_list = []
  for element in list1:
    if element not in union_list:
      union_list.append(element)
  for element in list2:
    if element not in union_list:
      union_list.append(element)
  return union_list

def intersection(list1, list2):
  """
  Finds the intersection of two lists.

  Args:
    list1: The first list.
    list2: The second list.

  Returns:
    A list containing all the elements that are in both list1 and list2.
  """
  intersection_list = []
  for element in list1:
    if element in list2:
      intersection_list.append(element)
  return intersection_list

def difference(list1, list2):
  """
  Finds the difference of two lists.

  Args:
    list1: The first list.
    list2: The second list.

  Returns:
    A list containing all the elements that are in list1 but not in list2.
  """
  difference_list = []
  for element in list1:
    if element not in list2:
      difference_list.append(element)
  return difference_list


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print("Union:", union(list1, list2))
print("Intersection:", intersection(list1, list2))
print("Difference:", difference(list1, list2))
