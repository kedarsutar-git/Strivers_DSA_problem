'''
Example 1

Input : Dividend = 10 , Divisor = 3
Output : 3
Explanation : 10/3 = 3.33 , truncated to 3.



Example 2

Input : Dividend = 7 , Divisor = -3
Output : -2
Explanation : 7/-3 = -2.33 , truncated to -2.
'''
class Solution:
    def Divide(Self,Dividend:int,Divisor:int):
        Sum = 0
        count = 0
        while(Sum+Divisor<=Dividend):
            count +=1
            Sum +=Divisor

        return count
object= Solution()
print(object.Divide(7,3))        
'''
Time Complexity:O(n)
Space Complexity:O(1)

'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Special case
        if dividend == divisor:
            return 1

        # Determine the sign of the answer
        sign = True
        if (dividend >= 0 and divisor < 0) or \
           (dividend < 0 and divisor > 0):
            sign = False

        # Work with positive numbers
        n = abs(dividend)
        d = abs(divisor)

        ans = 0

        # Repeatedly subtract using bit manipulation
        while n >= d:
            count = 0

            while n >= (d << (count + 1)):
                count += 1

            ans += (1 << count)
            n -= (d << count)

        # Apply the sign
        if not sign:
            ans = -ans

        # Handle overflow
        if ans > INT_MAX:
            return INT_MAX

        if ans < INT_MIN:
            return INT_MIN

        return ans
    
object = Solution()
print(object.divide(12,3))
'''
Time complexity:O((log n)²)
Space Complexity:O(1)

''' 