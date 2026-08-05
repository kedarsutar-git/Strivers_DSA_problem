from collections import deque

dq = deque()

dq.append(10)
dq.append(20)

dq.appendleft(5)

print(dq)

dq.pop()

dq.popleft()

print(dq)