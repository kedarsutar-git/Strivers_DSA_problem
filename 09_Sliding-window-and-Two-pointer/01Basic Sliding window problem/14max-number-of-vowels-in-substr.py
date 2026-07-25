'''
Given a string s and an integer k, return the maximum number of vowel 
letters in any substring of s with length k.
Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.


Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.


Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
'''

'''
Algorithm:


1.Expand window.
2.If right character is vowel → count += 1
3.When window size becomes k
 Update answer.
 Remove left character.
 If left character was vowel → count -= 1
 Move left.
Continue.
'''


# Brute force method 
class Solution:
    def maxvowels(self,nums:str,k:int) ->int:
        vowels = "aeiou"
        maxcount = 0
        for i in range(len(nums)):
            currentcount = 0
            for j in range(i,len(nums)):

                if(nums[j] in vowels):
                    currentcount += 1

                length = j-i+1
                if(length==k):
                    maxcount = max(maxcount,currentcount)

        return maxcount

object = Solution()
nums ="aeiou"
print(object.maxvowels(nums,2))

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''

# optimal method 

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowles = "aeiou"
        right,left = 0,0
        currentcount = 0
        maxcount = 0

        while(right<len(s)):

            if(s[right] in vowles):
                currentcount += 1

            if(right-left+1==k):
            
                maxcount = max(maxcount,currentcount)

                if(s[left] in vowles):
                    currentcount -= 1

                left += 1
            right += 1

        return maxcount

object = Solution()
s = "leetcode"
print(object.maxVowels(s,3))
              
'''
Time complexity:(n)
Space Complexity:O(1)

'''










