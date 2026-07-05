'''
Problem Statement: Given two integers L and R. Find the XOR of the elements in the range [L , R].

Examples
Example 1:
Input :
L = 3 , R = 5
Output :
 2
Explanation : 
answer = (3 ^ 4 ^ 5) = 2.


Example 2:
Input :
L = 1, R = 3
Output :
 0
Explanation : 
answer = (1 ^ 2 ^ 3) = 0.
'''
# Brute Force method 

class Solution:
    def FindXOR(self,L:int,R:int):
        l = []
        for i in range(L,R+1):
            l.append(i)

        ans = 0
        for num in l:
            ans  = ans^num

        return ans 

object = Solution()
print(object.FindXOR(1,3))  

'''
Time complexity:O(n)
Space complexity:O(n)
'''


# Better method 

class Solution:
    def FindXOR(self,L:int,R:int):
        ans = 0
        for i in range(L,R+1):
            ans = ans^i

        return ans 

object = Solution()
print(object.FindXOR(3,5))       

'''
Time complexity:O(n)
Space complexity:O(1)
'''

# Optimal method 
