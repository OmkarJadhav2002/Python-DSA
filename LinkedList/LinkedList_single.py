# Implemet Singly Linked-List


# Create a node class
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

    def insert_at_position(self, pos, value):
        # create new node
        new_node = Node(value)
        temp = self.head

        # if position 1
        if pos == 1:
            self.insert_at_first(value)
        # if position last
        if temp.next is None:
            self.insert_at_end(value)
        # for other positions
        else:
            current = self.head

            for i in range(pos - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    # Deletion Operations
    def delete_from_first(self):
        if self.head is None:
            print("Linked list is empty.")
        if self.head.next is None:
            self.head = None
        else:
            current = self.head
            self.head = current.next
            current.next = None

    def delete_from_last(self):
        if self.head is None:
            print("Empty linked list.")
            return

        # if self.head.next is None:
        #     self.head = None
        # else:
        #     current = self.head

        #     while current.next.next != None:
        #         current = current.next

        #     current.next = None

        # using two pointers
        temp1 = self.head  # (next)
        temp2 = self.head.next  # (prev)

        if temp1.next is None:
            self.delete_from_first()

        while temp2.next:
            temp1 = temp1.next
            temp2 = temp2.next

        temp1.next = None

    def delete_from_position(self, pos):
        temp = self.head
        if self.head is None:
            print("Empty Linked list.")

        if pos == 0:
            self.head = self.head.next
            return self.head
        else:
            # current = self.head
            temp = self.head.next
            prev = self.head

            for i in range(1, pos - 1):
                temp = temp.next
                prev = prev.next

            prev.next = temp.next
            temp.next = None

        # else:

        # else:
        #     if pos == 1:
        #         self.delete_from_first()
        #     elif temp.next is None:
        #         self.delete_from_last()
        #     else:
        #         for i in range(pos - 1):
        #             temp = temp.next

        #         temp.next = temp.next.next
        #         temp.next.next = None

    def delete_by_value(self, value):
        pass

    # Display Linked-List
    def display(self):
        res = ""  # to store the result

        current = self.head
        while current != None:
            res = res + str(current.data) + " -> "
            current = current.next

        return res[:-3]

    def count_nodes(self):
        count = 0

        current = self.head
        while current.next is not None:
            current = current.next
            count += 1

        return count


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_at_first(10)
    # ll.insert_at_first(20)
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("Linked list: ", ll.display())
    # ll.delete_from_first()
    # ll.delete_from_last()
    ll.delete_from_position(2)
    print("Linked list: ", ll.display())
    # print("Number of nodes: ", ll.count_nodes())
