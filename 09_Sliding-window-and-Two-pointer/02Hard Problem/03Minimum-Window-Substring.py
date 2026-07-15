'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring 
of s such that every character in t (including duplicates) is included in the window. If there 
is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.


Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

# Brute force 
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        # Frequency map of t
        freq = {}
        for ch in t:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        minLen = float('inf')
        startIndex = -1

        for i in range(len(s)):

            window = freq.copy()
            count = 0

            for j in range(i, len(s)):

                if s[j] in window and window[s[j]] > 0:
                    count += 1

                if s[j] in window:
                    window[s[j]] -= 1

                if count == len(t):

                    if j - i + 1 < minLen:
                        minLen = j - i + 1
                        startIndex = i

                    break

        if startIndex == -1:
            return ""

        return s[startIndex:startIndex + minLen]


s = "ADOBECODEBANC"
t = "ABC"

obj = Solution()
print(obj.minWindow(s, t))



# Brute force 
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        ans = ""
        minLen = float('inf')

        for i in range(len(s)):

            for j in range(i, len(s)):

                substring = s[i:j+1]

                # Check whether substring contains all characters of t
                temp = list(substring)
                found = True

                for ch in t:
                    if ch in temp:
                        temp.remove(ch)
                    else:
                        found = False
                        break

                if found:
                    if len(substring) < minLen:
                        minLen = len(substring)
                        ans = substring

        return ans


s = "ADOBECODEBANC"
t = "ABC"

obj = Solution()
print(obj.minWindow(s, t))


# Optimal method 

