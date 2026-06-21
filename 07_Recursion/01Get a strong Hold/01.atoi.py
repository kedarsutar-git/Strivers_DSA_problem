class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle empty string
        if i == n:
            return 0

        # Handle sign
        sign = 1

        if s[i] == '-':
            sign = -1
            i += 1

        elif s[i] == '+':
            i += 1

        def helper(index, num):

            # Base case
            if index >= n or not s[index].isdigit():
                return num

            digit = ord(s[index]) - ord('0')

            num = num * 10 + digit

            return helper(index + 1, num)

        ans = helper(i, 0)

        ans *= sign

        INT_MIN = -(2 ** 31)
        INT_MAX = (2 ** 31) - 1

        if ans < INT_MIN:
            return INT_MIN

        if ans > INT_MAX:
            return INT_MAX

        return ans

s = "  -12345"
object =Solution()
print(object.myAtoi(s))