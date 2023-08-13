class Node:
  def __init__(self, value):
    self.data = value
    self.next = None 

class Queue:
  def __init__(self):
    self.front = None
    self.rear = None 

  def isEmpty(self):
    return self.front == None 

  def enqueue(self, value):
    new_node = Node(value)
    if self.rear is None:
      self.front = new_node
      self.rear = self.front 

    else:
      self.rear.next = new_node 
      self.rear = new_node 

  def dequeu(self):
    if self.front is None:
      return "Empty Queue."
    else:
      self.front = self.front.next 

  def front_item(self):
    if self.front is None:
      return "Empty Queue."
    else:
      return self.front.data 

  def rear_item(self):
    if self.front is None:
      return "Empty Queue."
    else:
      return self.rear.data 

  def display(self):
    if self.front is None:
      print("Empty Queue.")
    else:
      temp = self.front 
      while temp:
        print(temp.data, end=' ') 
        temp = temp.next 

  def count_elements(self):
    count = 0
    temp = self.front 
    while temp:
      count += 1
      temp = temp.next 

    return count 
  
if __name__ == '__main__':
  q = Queue()
  q.enqueue(10)
  q.enqueue(20)
  q.enqueue(30)
  q.enqueue(40)
  q.enqueue(50)
  q.display()
  print("\nNumber of elements in queue: ", q.count_elements())
  # q.dequeu()
  # q.dequeu()
  print("First element: ", q.front_item())
  print("Rear element: ", q.rear_item())
  # print("Number of elements in queue: ", q.count_elements())
