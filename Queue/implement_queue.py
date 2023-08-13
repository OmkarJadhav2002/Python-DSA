queue = []


def enqueu():
    num = int(input("Enter the element to be inserted into the queue: "))
    queue.append(num)


def deque():
    if len(queue) == 0:
        print("Queue Underflow")
    else:
        queue.pop(0)


def display():
    if len(queue) == 0:
        print("Queue Underflow.")
    else:
        print("Elements in queue: ")
        for ele in queue:
            print(ele, end=" ")


def menu():
    while 1:
        print(
            """
      1. Enque Operation 
      2. Deque Operation 
      3. Display 
      4. Exit 
      """
        )

        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            print("Enque Operation")
            enqueu()
        elif user_input == 2:
            print("Deque Operation")
            deque()
        elif user_input == 3:
            print("Display")
            display()
        else:
            break


if __name__ == "__main__":
    menu()
