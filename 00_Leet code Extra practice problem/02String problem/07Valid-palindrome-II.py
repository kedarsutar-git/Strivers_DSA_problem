'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 
Example 1:

Input: s = "aba"
Output: true


Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.


Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
'''

class Solution:
    def validPalindrome(self,s:str) ->bool:
        def is_paindrome(start,end):

            while(start<end):
                if(s[start]!=s[end]):
                    return False
            
                start +=1
                end-=1

            return True

        start = 0
        end = len(s)-1

        while(start<end):
            if(s[start]!=s[end]):
                return is_paindrome(start+1,end) or is_paindrome(start,end-1)

            start +=1    
            end -=1

        return True
object =Solution()
s = "abca"
print(object.validPalindrome(s))

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''

