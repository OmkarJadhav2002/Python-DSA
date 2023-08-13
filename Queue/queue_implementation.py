# Using List
# queue = []

# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue)

# Pop from start
# queue.pop(0)
# queue.pop(0)
# queue.pop(0)

# print(queue)

# Using collections.deque
# from collections import deque

# q = deque()

# # Add elements to queue
# q.append(10)
# q.append(20)
# q.append(30)

# print(q)

# # Pop elements from queue
# q.popleft()

# print(q)


# Using queue.Queue
# from queue import Queue  # using inbuilt module

# # Queue(maxsize=0) # (if maxsize<=, then queue size is unlimited)
# qu = Queue(maxsize=7)

# put(item, block=True, timeout=None): adds item to the queue(enqueu)
# qu.put(10)
# qu.put(20)
# qu.put(30)
# qu.put(40)
# qu.put(50)
# qu.put(10)

# # Get the element
# print(qu.get())
# # Check queue empty or not
# print(qu.empty())
# # Check queue full or not
# print(qu.full())
# # Get the number of items in the queue
# print(qu.qsize())
