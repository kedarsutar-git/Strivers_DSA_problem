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
print(object.reverseWord(s))        \

class Solution:
    def reverseWord(self,string:str) ->str:

        words = s.split(" ")
        for word in words:
            wordarr = list(word)
            i = 0
            j = len(wordarr) - 1

            while(i<=j):
                wordarr[i],wordarr[j] = wordarr[j],wordarr[i]

                i += 1
                j -= 1

            "".join(wordarr)

        

object = Solution()
s = "Let's take LeetCode contest"
print(object.reverseWord(s))       




