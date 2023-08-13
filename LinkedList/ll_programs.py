# que 1: Write a Python program to find the maximum value in a linked list and replace it with the given value 
class Node:
  def __init__(self, value):  
    self.data = value 
    self.next = None 

class LinkedList:
  def __init__(self):
    self.head = None  

  # insert element into linked list  .append()
  def insert(self, value):
    new_node = Node(value)

    # if list is empty 
    if self.head == None:
      self.head = new_node 
      return 

    current = self.head 
    while current.next:
      current = current.next 

    current.next = new_node 

  # find the maximum element and replace it with given number 
  def replace_max(self, value):
    current = self.head 

    maxi = current 
    while current:
      if current.data > maxi.data:
        maxi = current 
      current = current.next 

    maxi.data = value 

  # Que. 2: return sum of elements that are at odd index (position) i.e. sum of odd nodes
  def add_odd_nodes(self):
    temp = self.head 
    # for counting the number of nodes 
    counter = 0
    # to store the result 
    res = 0

    while temp:
      if counter % 2 != 0:
        res += temp.data 

      temp = temp.next 
      counter += 1

    return res 

  # Reverse a linked list containing integer data (inplace reversal) 
  def reverse_list(self):
    prev = None 
    current = self.head 

    while current:
      temp = current.next 
      current.next = prev 
      prev = current 
      current = temp 

    self.head = prev 

  # displaying linked list 
  def display(self):
    current = self.head 
    res = ""
    while current: 
      res = res + current.data # + str(current.data) + ' -> '
      current = current.next 

    return res[:-3]

if __name__ == '__main__':
  l = LinkedList()
  # l.insert(10)
  # l.insert(20)
  # l.insert(30)
  # l.insert(40)
  # l.insert(50)
  l.insert("l")
  l.insert("l")
  l.insert("l")
  l.insert("l")
  l.insert("l")
  # l.insert(40)
  print("Linked list: ", l.display())
  l.reverse_list()
  print("Linked list in reverse order: ", l.display())
  # l.replace_max(100)
  # print("Linked list after replacing max element: ", l.display())
  # print("Sum of odd nodes: ", l.add_odd_nodes())