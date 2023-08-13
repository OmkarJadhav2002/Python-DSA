class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion Opearations
    def insert_at_first(self, value):
        # create new node
        new_node = Node(value)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, value):
        # create new node
        new_node = Node(value)

        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def insert_at_position(self, value, pos):
        # create new node
        new_node = Node(value)
        temp = self.head
        if pos == 1:
            self.insert_at_first(value)
        # elif temp.next is None:
        #     self.insert_at_end(value)
        else:
            pass

    # Deletion Operations
    def delete_from_first(self):
        pass

    def delete_from_end(self):
        pass

    def delete_from_position(self):
        pass

    # count number of nodes
    def count_nodes():
        current = self.head
        count = 0
        while current.next:
            current = current.next
            count += 1

        return count

    # Display LL
    def display(self):
        res = ""
        current = self.head
        while current:
            res = res + str(current.data) + " -> "
            current = current.next

        return res[:-3]


if __name__ == "__main__":
    ll = doublyLinkedList()
    # ll.insert_at_first(10)
    # ll.insert_at_first(20)
    # ll.insert_at_first(30)
    ll.insert_at_end(0)
    ll.insert_at_position(200, 1)
    ll.insert_at_position(12, 1)
    # ll.insert_at_end(90)
    print("Linked list: ", ll.display())
