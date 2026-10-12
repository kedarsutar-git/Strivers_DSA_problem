'''
Input: s = "BAABAABBBAAA", k = 2  
Output: 6  
Explanation: We can change the B at index 0 and 3 (0-based indexing) to A. 
The new string becomes "AAAAAABBBAAA". The substring "AAAAAA" is the longest substring with the same letter, and its length is 6. 


Input: s = "AABABBA", k = 1  
Output: 4  
Explanation: We can change one character to get the new string "AABBBBA". The substring "BBBB" is the longest with the same character.
There are other ways to achieve this result as well.
'''

class Solution:
    # Function to return the length of the longest substring that can be made of repeating characters
    # by replacing at most k characters
    def characterReplacement(self, s: str, k: int) -> int:

        # Dictionary to count frequency of characters in current window
        freq = {}

        # Left pointer of sliding window
        left = 0

        # Right pointer of sliding window
        right = 0

        # Stores max frequency of any char in current window
        max_freq = 0

        # Stores result
        max_len = 0

        # Traverse through each character with right pointer
        while(right<len(s)):

            # Increase frequency of current character
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Update the max frequency in current window
            max_freq = max(max_freq, freq[s[right]])

            # If window is invalid (more than k replacements)
            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            # Update max_len with current valid window size
            max_len = max(max_len, right - left + 1)
            
            right += 1
        return max_len


object = Solution()
s = "AABABBA"

print(object.characterReplacement(s, 1))

