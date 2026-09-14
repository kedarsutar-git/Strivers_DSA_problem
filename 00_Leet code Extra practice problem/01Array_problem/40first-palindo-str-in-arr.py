'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
'''
class Solution:
    def fun(self, s):
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True

    def firstPalindrome(self, words):
        for s in words:
            if self.fun(s):
                return s

        return ""

object = Solution()
words = ["abc","car","ada","racecar","cool"]
print(object.firstPalindrome(words))

'''
Time Complexity: O(n*m) where n is the number of strings in the array and m is the average length of the strings.
Space Complexity: O(1) since we are using a constant amount of space.
'''