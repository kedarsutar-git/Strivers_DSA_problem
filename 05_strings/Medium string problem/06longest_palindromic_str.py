'''
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.


Example 2:
Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for j in range(1,len(s)-1):
                if(s[i:j+1]==s[::-1]):
                    return s[i:j+1]
        return s[i:j+1]           

s = "kalam"       
object = Solution()
print(object.longestPalindrome(s))