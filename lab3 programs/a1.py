def pascal_triangle(n):
  """
  Prints out the first n rows of Pascal's triangle.

  Args:
    n: The number of rows to print.
  """
  triangle = [[1]]
  for i in range(1, n):
    row = [1]
    for j in range(1, i):
      row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    row.append(1)
    triangle.append(row)
  for row in triangle:
    print(row)


pascal_triangle(5)
