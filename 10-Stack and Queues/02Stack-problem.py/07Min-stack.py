class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((value, value))

        else:
            minval = min(value, self.stack[-1][1])
            self.stack.append((value, minval))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


object = MinStack()

print(object.stack)

object.push(5)
object.push(3)
object.push(7)
object.push(2)

print(object.stack)
print(object.top())
print(object.getMin())