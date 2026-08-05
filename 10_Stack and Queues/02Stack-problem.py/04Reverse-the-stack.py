'''
The problem statement for reversing a stack is:

Given a stack of integers, reverse the order of its elements.
After reversing, the top element of the original stack becomes the bottom element of the reversed stack, and vice versa.
The operation should be performed using stack-based logic, without converting it into another data structure such as a list or queue.
Example:

Input stack: [1, 2, 3, 4, 5]
Output stack: [5, 4, 3, 2, 1]
'''
class Solution:
    def reversestack(self, stack: list[int]) -> list[int]:
        if len(stack) <= 1:
            return stack

        top = stack.pop()
        self.reversestack(stack)
        self._insert_at_bottom(stack, top)
        return stack

    def _insert_at_bottom(self, stack: list[int], value: int) -> None:
        if not stack:
            stack.append(value)
            return

        top = stack.pop()
        self._insert_at_bottom(stack, value)
        stack.append(top)


stack = [1, 2, 3, 4, 5]
obj = Solution()
print(obj.reversestack(stack))


'''
Time Complexity: O(n^2) in the worst case due to recursive bottom insertions
Space Complexity: O(n) due to recursion stack

'''


