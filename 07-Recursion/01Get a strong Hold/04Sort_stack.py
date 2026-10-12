class Solution:
    def sort_stack(self, stack, x=None):
        if x is None:
            if not stack:
                return

            temp = stack.pop()
            self.sort_stack(stack)
            self.sort_stack(stack, temp)

        else:
            if not stack or stack[-1] <= x:
                stack.append(x)
                return

            temp = stack.pop()
            self.sort_stack(stack, x)
            stack.append(temp)


stack = [30, -5, 18, 14, 3]

obj = Solution()
obj.sort_stack(stack)

print(stack)