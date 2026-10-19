'''
You are given a string s consisting of lowercase English letters from 'a' to 'j'.

A substring is considered valid if at most one character occurs an odd number of times in that substring.

Return the total number of valid substrings in s.

A substring is a contiguous, non-empty sequence of characters within a string.

Example 1:
Input: s = "aba"

Output: 4

Explanation: The valid substrings are "a", "b", "a", and "aba". Each contains at most one character with an odd frequency.

Example 2:
Input: s = "aabb"

Output: 9

Explanation: There are 10 substrings in total. The only invalid substring is "ab", where both 'a' and 'b' occur an odd number of times. Hence, the answer is 9.
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)):
            
            for j in range(i+1,len(s)+1):
                
                substring = s[i:j]


                count_frq = {}
                for char in substring:
                    if char in count_frq:
                        count_frq[char] += 1

                    else:
                        count_frq[char] = 1

                odd_count = 0
                for value in count_frq.values():
                    if(value%2==1):
                        odd_count += 1

                if(odd_count<=1):
                    count += 1

        return count 


s = "aba"
object = Solution()
print(object.countSubstrings(s))

