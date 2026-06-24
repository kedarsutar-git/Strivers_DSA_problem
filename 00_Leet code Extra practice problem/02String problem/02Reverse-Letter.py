'''
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"


Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"


Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        start = 0
        end = len(s)-1
        s = list(s)
        while(start<=end):
            if(s[start] in char and s[end] in char):
                s[start],s[end] = s[end],s[start]

                start+=1
                end-=1

            elif(s[start] not in char):
                start+=1

            elif(s[end] not in char):
                end -=1

        return "".join(s)
    
s = "a-bC-dEf-ghIj"
object = Solution()
print(object.reverseOnlyLetters(s))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''