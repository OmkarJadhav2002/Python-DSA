# Implementing Singly Linked List
# Create Node class (Node is also a object)
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None  # address of next node (here it is null, because for only one node there is no address in next)


# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)

# n1.next = n2
# n2.next = n3

# print(n1.next)
# print(n2.next)
# print(n3.next)
# print(n1.data)
# print(n1.next.data)
# print(n2.next.data)
# print(n3.next)


class LinkedList:
    def __init__(self):
        # first node = called head
        self.head = None  # linked list is empty
        # for count of nodes
        self.n = 0

    # Insertion Operations
    # Insertion at beginning
    def insert_first(self, value):
        # Create a new node
        new_node = Node(value)

        # Create connection
        new_node.next = self.head

        # Reassign the head
        self.head = new_node

        # increment n
        self.n = self.n + 1

    # Insertion at last (tail) => append()
    def insert_last(self, value):
        # create a new node
        new_node = Node(value)

        # if linked list is empty
        if self.head is None:
            self.head = new_node
            self.n = self.n + 1
            return

        # at head first
        current = self.head
        # traverse till last node and stop at last node
        while current.next != None:
            current = current.next

        # you are at last node now, assign the address of new node in the next of current node i.e last node
        current.next = new_node

        self.n = self.n + 1

    # Insert after certain element
    def insert_after(self, after, value):
        new_node = Node(value)

        current = self.head
        while current is not None:
            if current.data == after:
                break
            current = current.next

        # case-1: break => item found (current is not none)
        if current != None:
            new_node.next = current.next
            current.next = new_node

            self.n = self.n + 1
        # case-2: item not found (current is none)
        else:
            print("Element not found.")

    # Insert at given position
    def insert_atPosition(self, pos, value):
        new_node = Node(value)
        current = self.head

        if pos == 1:
            self.insert_first(value)

        for i in range(pos - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # Deletion Operations
    def delete_list(self):
        self.head = None
        self.n = 0

        print("Linked List Deleted.")

    # delete from head (beginning)
    def delete_head(self):
        # self.head = self.head.next
        # or
        # if linked list is empty
        if self.head == None:
            print("List is empty.")
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None

        self.n = self.n - 1

    # delete from tail (ending) => pop()
    def delete_tail(self):
        # temp = self.head
        # while temp.next.next:
        #   temp = temp.next

        # # you are on second last node
        # temp.next = None

        # if list is empty
        if self.head == None:
            return "List is Empty."

        # using two pointer
        temp = self.head.next
        prev = self.head

        # if linked list has only one item
        if prev.next == None:
            return self.delete_head()

        while temp.next:
            temp = temp.next
            prev = prev.next

        prev.next = None

        self.n = self.n - 1

    # delete from given position
    def delete_from_position(self, pos):
        # using two pointers

        # if list is empty
        if self.head is None:
            return "List is empty."

        temp = self.head.next
        prev = self.head

        # if position is 0
        if pos == 0:
            self.head = self.head.next
            self.n = self.n - 1
            return self.head

        # for remaining conditions
        for i in range(1, pos - 1):
            temp = temp.next
            prev = prev.next

        prev.next = temp.next
        temp.next = None

        self.n = self.n - 1

    # Search an element
    def search(self, item):
        current = self.head
        pos = 0

        # traverse through linked list
        while current:
            if current.data == item:
                return pos

            current = current.next
            pos += 1

        return "Element not found."

    # Search by index position
    # def index_search(self, index):
    def __getitem__(self, index):
        current = self.head
        pos = 0
        while current:
            if pos == index:
                return current.data

            current = current.next
            pos += 1

        return "Invalid index position."

    # Linked list in reverse order  (to display linked list)
    # def traverse(self):
    def __str__(self):
        current = self.head
        res = ""

        while current != None:
            res = res + str(current.data) + " -> "
            current = current.next

        return res[:-3]
        # while current != None:
        #   print(current.data)
        #   current = current.next

        # To get the length of LinkedList

    def __len__(self):
        return self.n


if __name__ == "__main__":
    l = LinkedList()
    l.insert_first(1)
    # l.insert_first(2)
    # l.insert_first(3)
    # l.insert_first(4)
    # l.insert_first(5)
    # l.insert_last(10)
    # l.insert_last(20)
    # l.insert_last(30)
    # l.insert_last(40)
    # l.insert_last(50)
    # l.insert_after(100, 300)
    # l.delete_list()
    # l.delete_head()
    # l.delete_tail()
    # l.delete_tail()
    # l.delete_tail()
    # print(l.delete_tail())
    # l.delete_at_position()
    # l.delete_tail()
    # print("Element found at position {}".format(l.search(50)))
    # print("Element {} is at given index.".format(l.index_search(4)))
    # print(l[10])
    # print("Number of nodes in a linked list are: ", l.__len__())
    print("Linked list: ", l.__str__())
    # l.delete_from_position(1)
    # print("Linked list: ", l.__str__())
    # print(l.__len__())
