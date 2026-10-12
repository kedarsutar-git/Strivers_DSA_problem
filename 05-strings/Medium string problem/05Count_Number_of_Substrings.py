'''
Example 1:
Input:
s = "pqpqs", k = 2  
Output:
 7  
Explanation:
All substrings with exactly 2 distinct characters:  
"pq", "pqp", "pqpq", "qp", "qpq", "pqs", "qs"  
Total = 7.

Example 2:
Input:
s = "abcbaa", k = 3  
Output:
 5  
Explanation:
All substrings with exactly 3 distinct characters:  
"abc", "abcb", "abcba", "bcba", "cbaa"  
Total = 5.
'''
class Solution:
    def subarraysWithKDistinct(self, s: str, k: int) -> int:
    
        def atMostK(s, k):
            count = {}
            left = 0
            result = 0

            for right in range(len(s)):
                count[s[right]] = count.get(s[right], 0) + 1

                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1

                result += right - left + 1

            return result
        return atMostK(s, k) - atMostK(s, k - 1)
object = Solution()
s = "abcbaa"
print(object.subarraysWithKDistinct(s,2))  
'''
Time Compelxity:O(n**2)
Space Complexity:O(1)
'''  
    


