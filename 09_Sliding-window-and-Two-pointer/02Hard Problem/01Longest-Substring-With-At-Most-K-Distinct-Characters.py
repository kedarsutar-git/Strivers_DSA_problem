'''
Problem Statement:
Given a string s and an integer k.Find the length of the longest substring 
with at most k distinct characters

Ex:1
Input :s = "aababbcaacc" , k = 2
Output :6
Explanation :The longest substring with at most two distinct characters is "aababb".
The length of the string 6


Ex:2
Input : s = "abcddefg" , k = 3
Output : 4
Explanation : The longest substring with at most three distinct characters is "bcdd".
The length of the string 4.
'''

class Solution:
    def longestSubstr(self,s:str,k:int) ->int:
        maxlen = 0

        for i in range(len(s)):
            frq = {}
            for j in range(i,len(s)):
                if s[j] in frq:
                    frq[s[j]] += 1

                else:
                    frq[s[j]] = 1

                if(len(frq)>k):
                    break

                maxlen = max(maxlen,j-i+1)

        return maxlen

s = "aababbcaacc"
object = Solution()
print(object.longestSubstr(s,2))            

'''
Time Complexity:O(n**2)
Space Complexity:O(n)
'''

                
