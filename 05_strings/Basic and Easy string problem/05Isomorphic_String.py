'''
Example 1
Input:
s = "paper", t = "title"
Output:
true
Explanation:
 The characters in "s" can be mapped one-to-one to characters in "t": 
'p' → 't', 'a' → 'i', 'e' → 'l', 'r' → 'e'
Since the mapping is consistent and unique for each character, the strings are isomorphic.


Example 2
Input:
s = "foo", t = "bar"
Output:
false
Explanation:
'f' → 'b' is fine, 'o' → 'a' for the first 'o', But the second 'o' in "s" would need to map to 'r' in "t", which conflicts with the earlier mapping of 'o' → 'a'
This inconsistency makes it impossible to convert "s" to "t" using a one-to-one character mapping.
'''

class Solution:
    def IsomorphicString(self,s:str,t:str) -> bool:
        m1 = [0]*256
        m2 = [0]*256
        for i in range(len(s)):
            if(m1[ord(s[i])]!=m2[ord(t[i])]):
                return False
            
            m1[ord(s[i])] =i+1
            m2[ord(t[i])] =i+1

        return True
        
s = "paper" 
t = "title" 
object = Solution()
print(object.IsomorphicString(s,t)) 

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''