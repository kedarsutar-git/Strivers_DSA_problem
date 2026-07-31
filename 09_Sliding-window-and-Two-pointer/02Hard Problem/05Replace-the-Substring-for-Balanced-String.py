'''
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
 

Constraints:

n == s.length
4 <= n <= 105
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.
'''

from collections import defaultdict

class Solution:
    def balancedSubstr(self,s:str) ->int:

        target = len(s)//4
        count_map = defaultdict(int)

        for char in s:
            count_map[char] +=1

        if(count_map["Q"]==target and count_map["W"]==target and count_map["E"]==target and count_map["R"]==target):
            return 0

        left,right = 0,0
        minlen = len(s)


        while(right<len(s)):
            count_map[s[right]] -=1

            while(left<=right and count_map["Q"]<=target and count_map["W"]<=target and count_map["E"]<=target and count_map["R"]<=target):

                length = right -left + 1
                minlen = min(minlen , length)

                count_map[s[left]] +=1

                left +=1
            right +=1
        return minlen

s = "QQWE"
object = Solution()
print(object.balancedSubstr(s))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''