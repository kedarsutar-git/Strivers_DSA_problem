'''
a stack is typically a mutable data structure.

A stack allows changes over time via operations like push and pop.
'''

stack = []
stack.append(90)
stack.append(23)
stack.append(67)
stack.pop()

if len(stack) == 0:
    print("Empty")
else:
    print("Not Empty")

print("Length of stack:", len(stack))