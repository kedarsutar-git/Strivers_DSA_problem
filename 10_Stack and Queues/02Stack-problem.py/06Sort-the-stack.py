class Solution:
    def sortstack(self, stack: list[int]) -> list[int]:
        aux: list[int] = []

        while stack:
            value = stack.pop()
            while aux and aux[-1] > value:
                stack.append(aux.pop())
            aux.append(value)

        # aux now holds the sorted stack with smallest at bottom
        return aux

stack = [3, 4, 2, 5, 6]
solution = Solution()
print(solution.sortstack(stack))


