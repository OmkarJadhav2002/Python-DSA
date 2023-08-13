# Implementation Of Circular Linked List 
class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None 

class CircularLinkedList:
  def __init__(self):
    self.head = None 
    # self.tail = None 
    # store the count of nodes 
    self.n = 0

  # Insertion Operations 
  # a. Insert at beginning 
  def insert_at_first(self, value):
    new_node = Node(value)
    current = self.head 
    # now the head is new_node 
    new_node.next = self.head 

    # if the inserted node is the only node in list (list is empty)
    # Linked list is empty 
    if self.head is None:
      new_node.next = new_node  
      # return
    # at least one node in list  
    else:
      while current.next != self.head:
        current = current.next 
      current.next = new_node 
    # new_node is head now 
    self.head = new_node 

  # b. Insert at last 
  def insert_at_end(self, value):
    new_node = Node(value)
    # list is empty (inserted node is the only node in list)
    if self.head is None:
      self.head = Node(value)
      self.head.next = self.head 
    # if there are more than one node in list 
    else: 
      current = self.head 
      while current.next != self.head:
        current = current.next 

      current.next = new_node 
      new_node.next = self.head 

  # c. Insert at given position 
  def insert_at_position(self, pos, value):
    node_count = self.count_nodes()
    if pos < 1 or pos > node_count+1:
      return "Invalid position."
    elif pos == 1:
      return self.insert_at_first(value)
      self.n += 1
    elif pos > 1 or pos < (count_node):
      new_node = Node(value)
      current = self.head

      # not solved 
      for i in range(1, pos-1):
        current = current.next 

      new_node.next = current.next 
      current.next = new_node 

  # Deletion Operations 
  # a. Delete from beginning
  def delete_first(self):
    if self.head is None:
      return "Circular Linked List is empty."
    else:
      # if there is single node in list 
      if self.head == self.tail:
        self.head = None 
      # if there are more than one node in list 
      else:
        temp = self.head 
        self.head = temp.next 
        # delete the first node 
        temp = None 
        self.tail.next = self.head 
      
  # b. Delete from end 
  def delete_last(self):
    pass 

  # c. Delete from given position
  def delete_from_position(self, pos):
    pass 

  # Count the number of nodes  
  def count_nodes(self):
    return self.n 

  # display linked list 
  def display(self):

    if self.head is None:
      return "Circular Linked List is empty."

    # current = self.head 
    # print("Circular Linked List: ", end=" ")
    # print(current.data, '->', end=' ')
    # while current.next != self.head:
    #   current = current.next 
    #   print(current.data, '->', end=' ')

    current = self.head 
    res = ""
    while current:
      res = res + str(current.data) + ' -> '
      current = current.next 
      if current == self.head:
        break 

    return res[:-3]


if __name__ == '__main__':
  cl = CircularLinkedList()
  # cl.insert_at_end(10)
  cl.insert_at_end(20)
  cl.insert_at_end(200)
  cl.insert_at_first(100)
  # cl.insert_at_first(90)
  # cl.insert_at_first(89)
  # cl.insert_at_first(10)
  print(cl.display())
  # print("Circular Linked List: ", cl.display())
  # cl.delete_first()
  # print("Circular Linked List: ", cl.__str__())

