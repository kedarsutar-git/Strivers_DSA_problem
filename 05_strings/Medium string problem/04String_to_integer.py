'''
Example 1:
Input:
s = " -12345"  
Output:
-12345 

Explanation:
Ignore leading whitespaces.  
The sign '-' is encountered, indicating the number is negative.  
Digits 12345 are read and converted to -12345.

Example 2:
Input:
s = "4193 with words"  
Output:
4193  

Explanation:
Read the digits 4193 and stop when encountering the first non-digit character (w).
'''

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        num = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
            

s = "1233 kedar" 
object = Solution()
print(object.myAtoi(s))

'''
Time Complexity:O(n)
Space Compexity:O(1)
05
'''
