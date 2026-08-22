class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(digit) for digit in str(n)]
        sumdigits = sum(digits)
        productdigits = 1
        for num in digits:
            productdigits *= num

        if(n%(productdigits+sumdigits)==0):
            return True

        else:
            False

object = Solution()
print(object.checkDivisibility(99))

'''
Time Complexity:O(n)
Sapce Complexity:O(1)
'''