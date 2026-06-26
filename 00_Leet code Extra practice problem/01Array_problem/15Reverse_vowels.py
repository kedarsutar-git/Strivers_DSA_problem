'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''

class Solution:
    def ReverseVowels(self,s:str) ->str:
        s = list(s)

        vowels = "aeiouAEIOU"

        start = 0
        end = len(s)-1

        while(start<end):
            if(s[start] in vowels and s[end] in vowels):
                s[start],s[end] = s[end],s[start]

                start +=1
                end -=1

            elif(s[start] not in vowels):
                start +=1

            else:
                end -=1

        return "".join(s)

s = "IceCreAm"
object = Solution()
print(object.ReverseVowels(s))

'''
Time Complexity:O(n)
Space Compexilty:O(1)

'''



