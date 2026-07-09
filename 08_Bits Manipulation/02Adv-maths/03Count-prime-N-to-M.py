'''
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Example 2:
Input: n = 0
Output: 0


Example 3:
Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
'''


# Brute Force method 

class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2,n):
            if self.isPrime(i):
                count += 1

        return count 


    def isPrime(self,num):
        if(num<2):
            return False 

        for j in range(2,num):
            if(num%j==0):
                return False 

        return True 
    
object = Solution()
print(object.countPrimes(10))    

'''
Time Complexity:O(n**2))
Space Complexity:O(n)

'''