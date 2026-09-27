'''
You are given a string s consisting of one or more words separated by single spaces. Your task is to capitalize the first and last character of each word in the string.

If a word contains only one character, capitalize that character.

Return the transformed string after applying the operation to all words.

Example 1:
Input: s = "take u forward is awesome"

Output: "TakE U ForwarD IS AwesomE"

Explanation: Each word's first and last characters are capitalized.

Example 2:
Input: s = "Take u Forward is Awesome"

Output: "TakE U ForwarD IS AwesomE"

Explanation: Already capitalized characters remain, others are capitalized.


'''
class Solution:
    def capitalize_first_last(self, s: str) -> str:
        words = s.split(" ")
        result = []
        for word in words:
            if len(word) == 1:
                result.append(word.upper())
            else:
                result.append(word[0].upper() + word[1:-1] + word[-1].upper())

        return " ".join(result)
    
s ="take u forward is awesome"
object = Solution()
print(object.capitalize_first_last(s))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''