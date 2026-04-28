'''
Example 1:
Input:
s = "xyx"
Output:
 1
Explanation:
The substrings with non-zero beauty are:
"xyx" → frequencies: x:2, y:1 → beauty = 2 - 1 = 1
"xy" → x:1, y:1 → beauty = 0
"yx" → y:1, x:1 → beauty = 0
"x" or "y" → beauty = 0
Total sum = 1 (from "xyx") = 1


Example 2:
Input:
s = "aabcbaa"
Output:
17
Explanation:
Various substrings such as "aabc", "bcba", etc., have non-zero beauty values. Summing all gives 17.
'''
s = "abc"
class Solution:
    def beauty_sum(self,s):
        total = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1

                values = freq.values()
                maxi = max(values)
                mini = min(values)

                total += (maxi - mini)

        return total
s = "xyx"
object =Solution()
print(object.beauty_sum(s))
