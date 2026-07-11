'''
Length of Longest Substring without any Repeating Character

Example 1:
Input:S = "abcddabac"  

Output:4  

Explanation:
The longest substring with distinct characters is "abcd", 
which has a length of 4.


Example 2:
Input:S = "aaabbbccc" 

Output:2  

Explanation:
The longest substrings with distinct characters are "ab" and 
"bc", both having a length of 2.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while(s[right] in seen):
                seen.remove(s[left])

                left += 1

            seen.add(s[right])
            max_len = max(max_len,right - left + 1)

        return max_len        
        
object = Solution()
s = "aaabbbccc"
print(object.lengthOfLongestSubstring(s))

'''
Time Complexity:O(n)
Space Complexity:O(n)

'''