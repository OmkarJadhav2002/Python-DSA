# Implementing doubly linked list  
class Node:
  def __init__(self, value):
    self.prev = None 
    self.next = None 
    self.data = value 

class DoublyLinkedList:
  def __init__(self):
    # intially list is empty 
    self.head = None 
    # to maintain the count of nodes 
    self.n = 0

  # Insertion Operations 
  # Insert at first/head (insert at head => .prepend()) 
  def insert_at_first(self, value):
    # create new node 
    new_node = Node(value)

    # if list is empty 
    if self.head is None:
      new_node.prev = None 
      self.head = new_node 
      
      self.n += 1

    # otherwise 
    else:
      new_node.next = self.head 
      self.head.prev = new_node 
      self.head = new_node 
      new_node.prev = None 

      # or 
      # temp = self.head 
      # self.head.prev = new_node
      # new_node.next = self.head 
      # self.head = new_node 

      self.n += 1

  # Insert at end/tail (.append())
  def insert_at_end(self, value):  
    new_node = Node(value)

    # if list is empty and new_node is the first node 
    if self.head is None:
      new_node.prev = None 
      self.head = new_node  

    temp = self.head 
    while temp.next:
      temp = temp.next
      
    temp.next = new_node 
    new_node.prev = temp
    new_node.next = None  

    self.n += 1

  # Insert at given position 
  def insert_at_position(self, pos, value):
    # create new node 
    count_node = self.node_count()

    if pos < 1 or pos > (count_node+1):
      print("Invalid Position.")
      return 
    if pos == 1:
      self.insert_at_first(value)
      self.n += 1
    elif pos > 1 or pos < (count_node-1):
      new_node = Node(value)
      temp = self.head 
      for i in range(1, pos-1):
        temp = temp.next 

      new_node.prev = temp 
      new_node.next = temp.next 
      # temp.next.prev = new_node 
      temp.next = new_node 

      # not understood 
      # if the position is last (inserting at end position)
      if temp.next:
        temp.next.prev = new_node 

      self.n += 1

    # elif pos == count_node-1:
    #   self.insert_at_end(value)

  # Insert after certain element 
  def insert_after(self, key, data):
    new_node = Node(data)
    current = self.head 
    while current:
      # if there is one node in list 
      if current.next is None and current.data == key:
        self.insert_at_end(data)
        return 
      elif current.data == key:
        temp = current.next # store the address of the next node (to manipulate the remaining pointers)
        current.next = new_node 
        new_node.next = temp 
        new_node.prev = current 
        temp.prev = new_node  

      # update the current pointer 
      current = current.next 

  # Insert before certain element 
  def insert_before(self, key, data):
    new_node = Node(data)
    current = self.head 

    while current:
    # if there is one node in list 
      if current.prev is None and current.data == key:
        self.insert_at_first(data)
        return 
      elif current.data == key:
        temp = current.prev
        temp.next = new_node 
        current_prev = new_node 
        new_node.next = current 
        new_node.prev =  temp 
      
      current = current.next 

  # Deletion Operations 
  # Delete from head/first 
  def delete_first(self):
    # edge case 
    current = self.head 
    if current == self.head:
      if not current.next: # not pointing to any node (single node in list)
        current = None 
        self.head = None 
        return 
      else: # pointing to node 
        temp = current.next  
        current.next = None 
        temp.prev = None 
        current = None # pahila pointer cha address ch udun takla (sampla wishay)
        self.head = temp 
        return 

  # Delete from tail/last (.pop())
  def delete_last(self):
    current = self.head
    if self.head == None:
      return "Linked list is empty."
    # edge case: only one node 
    elif not current.next:
      current = None 
      self.head = None 
      return 
    else:
      temp = current.next 
      before = self.head 

      while temp.next:
        temp = temp.next 
        before = before.next 

      before.next = None 
      temp.next = None 

  # Delete from given position 
  def delete_from_position(self, pos):
    count_node = self.node_count()

    if pos < 1 or pos > (count_node+1):
      return "Invalid Position."
    elif pos == 1:
      self.delete_first()
      return 
    else:
      current = self.head.next  
      before = self.head 

      for i in range(1, pos-1):
        current = current.next 
        before = before.next 

      before.next = current.next 
      current.next.prev = before  
      current.prev = None
      current.next = None 
      return  

  def node_count(self):
    return self.n  

  # display linked list 
  def display(self):
    # if linked list is empty 
    if self.head is None:
      print("Linked list is empty.")
    
    temp = self.head 
    res = ""
    while temp:
      res = res + str(temp.data) + ' -> '
      temp = temp.next 

    return res[:-3]

if __name__ == '__main__':
  l = DoublyLinkedList()
  l.insert_at_end(10)
  l.insert_at_end(20)
  l.insert_at_end(30)
  # l.insert_at_end(40)
  # l.insert_at_end(50)
  # l.insert_at_first(9)
  print(l.display())

  # l.insert_before(9, 90)
  # l.delete_first()
  # l.delete_last()
  l.delete_from_position(3)
  print(l.display())