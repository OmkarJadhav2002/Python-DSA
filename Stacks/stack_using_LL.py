# Implementation of stack using Linked List 

class Node:
  def __init__(self, value):
    self.next = None 
    self.data = value 

class Stack:
  def __init__(self):
    # top most element 
    self.top = None 

  # check for stack is empty or not (False = stack not empty, True = stack empty)
  def isEmpty(self):
    return self.top == None

  # push the element into stack 
  def push(self, value):
    new_node = Node(value)
    new_node.next = self.top 
    self.top = new_node 

  # pop the element from stack 
  def pop(self):
    if self.isEmpty():
      return "Stack Underflow."
    
    else:
      self.top = self.top.next  

  # get the top most element from stack 
  def peek(self):
    if self.isEmpty():
      return "Stack Underflow."

    return self.top.data

  # get the number of elements in stack 
  def size(self):
    temp = self.top 
    count = 0
    while temp:
      count += 1
      temp = temp.next 

    return count 

  # Display the stack 
  def display(self):
    temp = self.top
    while temp:
      print(temp.data) 
      temp = temp.next 

if __name__ == '__main__':
  s = Stack()
  # print(s.isEmpty())
  s.push(10)
  s.push(20)
  # s.push(30)
  s.push(40)
  s.push(50)
  s.display()
  # s.pop()
  print("Number of elements in stack: ", s.size())
  # print(s.peek())
  # s.display()
