from collections import deque
queue = deque()

queue.append(12)
queue.append(1)
queue.append(23)
queue.append(45)
print(queue)


# Front (first number in the queue)
print("Front:",queue[0])


# Rear (last number in the queue)
print("Rear",queue[-1])

# Dequeue (is the operation not Data str removing element in the queue)
removed = queue.popleft()
print("Removed:",removed)

print("Queue :", queue)

# Size
print("Size :", len(queue))

# Empty Check
if not queue:
    print("Queue Empty")
else:
    print("Queue Not Empty")




'''
| Feature   | Stack                         | Queue                               |
| --------- | ----------------------------- | ----------------------------------- |
| Rule      | LIFO                          | FIFO                                |
| Insert    | Top                           | Rear                                |
| Remove    | Top                           | Front                               |
| Real Life | Stack of plates               | People in line                      |
| Python    | `list.append()`, `list.pop()` | `deque.append()`, `deque.popleft()` |

'''

