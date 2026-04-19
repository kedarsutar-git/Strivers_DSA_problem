'''
Example :1

str = ["flower", "flow", "flight"]
Output:"fl"
Explanation:
All strings in the array begin with the common prefix "fl".

Example 2

str = ["apple", "banana", "grape", "mango"]
Output: ""
Explanation:
None of the strings share a common starting sequence, so the result is an empty string.
'''
class Solution:
    def LongestCommenFrefix(self,s:str) -> str:
        if(not s):
            return ""
        s.sort()
        s1 = s[0]
        s2 = s[len(s)-1]
        ans = []
        for i in range(min(len(s1),len(s2))):
            if(s1[i]!=s2[i]):
                return ''.join(ans)
            ans.append(s1[i])
              
        return ''.join(ans)         

           
s = ["flowers" , "flow" , "fly", "flight" ]
object = Solution()
print(object.LongestCommenFrefix(s))            


'''
Time Complexity:O(nlogn⋅m+m)
Space Compexity:O(m)
'''