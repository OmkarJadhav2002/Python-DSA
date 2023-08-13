# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))

# # take the input from user
# print("Enter the elements: ")
# arr = []
# for i in range(row):
#   r = []
#   for j in range(col):
#     r.append(int(input()))

#   arr.append(r)

# # display the matrix 
# print("Matrix: ")
# for i in range(row):
#   for j in range(col):
#     print(arr[i][j], end=" ")
#   print()


# def find_largest_row(arr, row, col):
#   maxi = float('-inf') # equivalent to "INT-MIN" of C++
#   rowIndex = -1
#   for i in range(row):
#     sum = 0
#     for j in range(col):
#         sum += arr[i][j]

#     if sum > maxi:
#       maxi = sum
#       rowIndex = row

#   print("Maximum sum is: ", maxi)
#   return rowIndex
    
# print(find_largest_row(arr, row, col))


# def wavePrint(arr, nRows, mCols):
#   for j in range(mCols):
#       # if the column index is even 
#       if j%2 == 0:
#           for i in range(nRows):
#             print(arr[i][j], end=" ")
#       # if the column index is odd 
#       else:
#           for i in range(nRows-1, -1, -1):
#               print(arr[i][j], end=" ")


# wavePrint([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)

