# Implementing stack using linked list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    # get top element
    def peek(self):
        if self.isEmpty():
            return "Stack underflow"
        else:
            return self.top.data

    def pop(self):
        if self.isEmpty():
            return "Stack underflow"
        else:
            self.top = self.top.next

    def isEmpty(self):
        return self.top == None

    def display(self):
        temp = self.top

        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(12)
    stack.push(100)
    stack.display()
    stack.pop()
    print()
    stack.display()

    # print(stack.isEmpty())
