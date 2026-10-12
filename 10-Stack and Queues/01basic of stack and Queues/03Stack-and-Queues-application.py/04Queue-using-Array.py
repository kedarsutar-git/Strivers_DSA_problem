class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, x):  # push 
        self.queue.append(x)

    def dequeue(self):  # pop
        if not self.queue:
            return "Queue Underflow"
        return self.queue.pop(0)

    def front(self):  # peek
        if not self.queue:
            return "Queue Underflow"
        return self.queue[0]

    def rear(self): 
        return self.queue[-1]

    def display(self):
        print(self.queue)


# Example
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print(q.dequeue())