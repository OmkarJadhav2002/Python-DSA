# find the row wise sum

row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

# take the input from user
print("Enter the elements: ")
matrix = []
for i in range(row):
  r = []
  for j in range(col):
    r.append(int(input()))

  matrix.append(r)

# display the matrix 
print("Matrix: ")
for i in range(row):
  for j in range(col):
    print(matrix[i][j], end=" ")
  print()
  
# find the row-wise sum 
def find_row_sum(matrix, row, col):
  print("Row-wise sum: ")
  for i in range(row):
    sum = 0
    for j in range(col):
      sum += matrix[i][j]

    print(sum, end=" ")

# find column-sum 
def find_col_sum(matrix, row, col):
  print("\nColumn-wise sum: ")
  for i in range(col):
    sum = 0
    for j in range(row):
      sum += matrix[j][i]

    print(sum, end=" ")

find_row_sum(matrix, row, col)
find_col_sum(matrix, row, col)