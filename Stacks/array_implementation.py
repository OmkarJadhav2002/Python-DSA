# My Logic
# class Stack:
#   def __init__(self):
#     self.s = list()

#   def push(self, data):
#     self.s.append(data)

#   def pop(self):
#     print("\nPopped element: ", end="")
#     if self.isEmpty():
#       return "Stack is empty."
#     else:
#       return self.s.pop()

#   def top(self):
#     if self.isEmpty():
#       return "Stack is empty."
#     else:
#       return self.s[-1]

#   def display(self):
#     print("Stack elements are: ", end="")
#     for ele in self.s:
#       print(ele, end=" ")

#   def isEmpty(self):
#       return len(self.s) == 0


# Love Babbar video
class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.top = -1

    def push(self, item):
        # check if space is available or not
        if self.size - self.top > 1:
            self.top += 1
            self.array[self.top] = item
        else:
            print("Stack Overflow.")

    def pop(self):
        if self.top >= 0:
            self.top -= 1
        else:
            return "Stack Underflow."

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if self.top >= 0:
            return self.array[self.top]
        else:
            print("Stack is empty.")
            return -1

    def display(self):
        print("Elements in stack: ", end="")
        for ele in range(len(self.array)):
            print(self.array[ele], end=" ")


if __name__ == "__main__":
    stack = Stack(5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.display()
    stack.push(89)
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.top())


# class Stack:
#   def __init__(self):
#     self.arr = []

# def push(self):
#   return self.arr.insert(0, data)

# def pop(self):
#   return self.arr.pop(0)
