'''
Example 1:
Input: CAT, ACT
Output: true
Explanation: Since the count of every letter of both strings are equal.


Example 2:
Input: RULES, LESRT 
Output: false
Explanation: Since the count of U and T  is not equal in both strings.
'''

class Solution:
    def anagrams(self,s:str,t:str) -> bool:
        
        if(len(s)!=len(t)):
            return False
        
        if(sorted(s)==sorted(t)):
            return True
        return False    
                
        
                      
s = "CAT"
t = "ACT"
object =Solution()
print(object.anagrams(s,t))   
 
'''
Time Complexity:O(NlogN)
space Complexity:O(1)

'''


     
