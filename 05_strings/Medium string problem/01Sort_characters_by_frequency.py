'''
Example 1:
Input:
s = "tree"
Output:
 ['e', 'r', 't']
Explanation:

e → 2
r → 1
t → 1
Since 'r' and 't' have the same frequency, they are sorted alphabetically → 'r' comes before 't'.



Example 2:
Input:
s = "raaaajj"
Output:
 ['a', 'j', 'r']
Explanation:

a → 4
j → 2
r → 1
Characters are sorted by decreasing frequency. In case of ties, alphabetically.
'''

class Solution:
    def SortChar(self,s:str) -> list[int]:
        S = set()
        for i in range(len(s)):
            S.add(s[i])
            l = list(set(S))
            l.sort()

        return l
s = "raaaajj"  
object =Solution()
print(object.SortChar(s))

'''
Time Complexity:O(n)
Space Complexity:O(n) # for set
'''
            



