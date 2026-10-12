'''
Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"


Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.



Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
class Solution:
    def reverseWord(self,s:str) ->str:
        words = []
        word = ""
        for ch in s:
            if ch != " ":
                word += ch
            elif word:
                words.append(word)
                word = ""
        
        if word:
            words.append(word)
        
        words.reverse()
        
        return " ".join(words)
            
word = "kedar is good boy"
object = Solution()
print(object.reverseWord(word))                