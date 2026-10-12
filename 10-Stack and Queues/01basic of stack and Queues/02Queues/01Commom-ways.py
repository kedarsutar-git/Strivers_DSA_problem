# List(Good for learning but not efficient)
queues =[]

# 2.deque

from collections import deque
queue = deque()



# 3.queue.Queue

from queue import Queue
q = Queue()



# Note: For DSA and coding interviews, use collections.deque.


# Why we not use List
queue = [10, 20, 30, 40]

queue.append(10)
print("Before pop:", queue)   # [10, 20, 30, 40, 10]

queue.pop(0)
print("After pop:", queue)    # [20, 30, 40, 10]
# pop(0) removes the first element and shifts all remaining elements to the left.

'''
Before pop: [10, 20, 30, 40, 10]
After pop: [20, 30, 40, 10]
'''
