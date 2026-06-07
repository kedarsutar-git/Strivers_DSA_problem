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
    def SortChar(self,s:str):
        S = set()
        for i in range(len(s)):
            S.add(s[i])
            l = list(set(s))
            l.sort()

        return l

s = "tree"
object =Solution()
print(object.SortChar(s))  

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''

'''
Example 1:
Input:
s = "(1+(2*3)+((8)/4))+1"
Output:
3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input:
s = "(1)+((2))+(((3)))"
Output:
3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.
'''

class Solution:
    def MaxDepth(self,s:set) ->int:
        Max_depth = 0
        Current_depth = 0
        for brac in s:
            if(brac=="("):
                Current_depth +=1
                Max_depth = max(Max_depth,Current_depth)

            elif(brac==")"):
                Current_depth -=1

        return Max_depth 

s = "(1)+((2))+(((3)))"
object = Solution()
print(object.MaxDepth(s))

