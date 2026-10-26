'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''



        
class Solution:
    def reverseWord(self,string:str) ->str:

        words = s.split(" ")
        return " ".join(word[::-1] for word in words)
    

object = Solution()
s = "python"
print(object.reverseWord(s))       



class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        ans = ""

        for word in words:
            ans += word[::-1] + " "

        return ans.strip()

s = "i love python"
obj = Solution()
print(obj.reverseWords(s))