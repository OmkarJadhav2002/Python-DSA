# how to take input of 2d array 
# n = int(input("Enter a number: "))
# arr = []

# for i in range(n):
#   arr.append([int(j) for j in input().split()])

# print(arr)3

# n = int(input()) 
# a = []
# for i in range(n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = row[i]
#     a.append(row)
# print(a)

# row = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))
# matrix = []
# taking input from the user
# for i in range(row):
#     r = []
#     for j in range(col):
#         r.append(int(input()))

#     matrix.append(r)

# display the matrix row wise
# for i in range(row):
#     for j in range(col):
#         print("Matrix:\n", matrix[i][j], end=" ")
#     print()


# display the matrix column wise 
# print("Matrix:\n")
# for i in range(col):
#     for j in range(row):
#         print(matrix[j][i], end=" ")
#     print()

# find the element is present in matrix or not 
row = int(input("Enter number of rows: "))
col = int(input("Enter number of columns: "))
matrix = []
for i in range(row):
    r = []
    for j in range(col):
        r.append(int(input()))

    matrix.append(r)

# display the matrix 
for i in range(row):
    for j in range(col):
        print(matrix[i][j], end=" ")
    print()


target = int(input("Enter the element want to search: "))
def find_element(matrix, target, row, col):
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == target:
                return True

        return False

if find_element(matrix, target, row, col) == True:
    print("Element found.")
else:
    print("Element not found.")
    