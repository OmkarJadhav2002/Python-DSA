
            current = self.head

            for i in range(pos - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node
