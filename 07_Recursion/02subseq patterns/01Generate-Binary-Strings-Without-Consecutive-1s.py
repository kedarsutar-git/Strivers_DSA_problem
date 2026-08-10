class Solution:
    def generateBinaryStrings(self, n):
        ans = []

        def backtrack(curr):
            # Base case
            if len(curr) == n:
                ans.append(curr)
                return

            # Always place '0'
            backtrack(curr + "0")

            # Place '1' only if previous character is not '1'
            if len(curr) == 0 or curr[-1] != "1":
                backtrack(curr + "1")

        backtrack("")
        return ans
    
n = 3
object = Solution()
print(object.generateBinaryStrings(n))
    