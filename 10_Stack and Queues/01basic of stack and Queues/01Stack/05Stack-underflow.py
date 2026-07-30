# Handling stack underflow safely

stack = []

if not stack:
    print("Stack underflow: cannot pop from an empty stack")
else:
    print("Popped:", stack.pop())


'''
| Pseudocode   | Python Code       | Time Complexity |
| ------------ | ----------------- | --------------- |
| Create Stack | `stack = []`      | O(1)            |
| Push(x)      | `stack.append(x)` | O(1)            |
| Pop()        | `stack.pop()`     | O(1)            |
| Peek()       | `stack[-1]`       | O(1)            |
| isEmpty()    | `not stack`       | O(1)            |
| Size()       | `len(stack)`      | O(1)            |

'''



stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("After Push :", stack)

# Peek
print("Top Element :", stack[-1])

# Pop
removed = stack.pop()
print("Removed :", removed)

print("After Pop :", stack)

# Size
print("Size :", len(stack))

# Empty Check
if not stack:
    print("Stack is Empty")
else:
    print("Stack is Not Empty")