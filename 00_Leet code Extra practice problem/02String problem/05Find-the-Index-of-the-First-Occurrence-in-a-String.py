'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.



Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution:
    def Findindex(self,s1:str,s2:str) ->int:
        for i in range(len(s1)-len(s2)+1):
            j = 0

            while(j<len(s2) and s1[i+j]==s2[j]):
                j+=1

            if(j==len(s2)):
                return i

        return -1

s1 = "sadbutsad"
s2 = "sad"
object = Solution()
print(object.Findindex(s1,s2))

'''
Time Complexity:O(n*m)
Space Complexity:O(1)

'''