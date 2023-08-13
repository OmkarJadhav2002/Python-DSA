# Reverse a string using Stack

st = input("Enter a string: ")

stack = []
for i in range(len(st)):
    stack.append(st[i])

res = ""
while len(stack):
    res += stack[-1]

    stack.pop()

print("Reversed string: ", res)
