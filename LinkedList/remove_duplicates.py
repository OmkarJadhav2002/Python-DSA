class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create a Linked-List class
class LinkedList:
    def __init__(self):
        self.head = None  # intially it is null/none

    # Insertion Operations
    def insert_at_first(self, value):
        # create a new node
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, value):
        # create a new node
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = new_node

    # remove duplicate
    def remove_duplicate(self):
        current = self.head
        temp = None
        while current and current.next:
            temp = current

            while temp.next:
                if current.data == temp.next.data:
                    temp.next = temp.next.next

                else:
                    temp = temp.next

            current = current.next
        return self.head

    def display(self):
        res = ""  # to store the result

        current = self.head
        while current != None:
            res = res + str(current.data) + " -> "
            current = current.next

        return res[:-3]


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_first(5)
    ll.insert_at_end(2)
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    # ll.insert_at_end(2)
    # ll.insert_at_end(2)
    print("Linked list: ", ll.display())
    ll.remove_duplicate()
    print("Linked list: ", ll.display())
