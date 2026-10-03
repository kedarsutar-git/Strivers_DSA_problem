'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        if n == 0:
            return []

        res = []
        stack = [("", 0, 0)]

        while stack:
            current, open_count, close_count = stack.pop()

            if len(current) == 2 * n:
                res.append(current)
                continue

            if close_count < open_count:
                stack.append((current + ")", open_count, close_count + 1))
            if open_count < n:
                stack.append((current + "(", open_count + 1, close_count))

        return res

object = Solution()
n = 3
print(object.generateParenthesis(n))

'''
Time Complexity:O(4^n/sqrt(n))
Space Complexity:O(4^n/sqrt(n))

'''