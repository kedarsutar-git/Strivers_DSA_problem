# Brute Force method
class Solution:
    def Sq_root(self,num:int) -> int:
        ans = 1
        for i in range(1,num+1):
            if(i*i<=num):
                ans = i

            else:
                break    

        return ans
object = Solution()
print(object.Sq_root(23))  

'''
Time Complexity:O(n)
Space ComplexityLO(1)
'''

# Use Binary Search
class Solution:
    def sqr_root(self, num:int) -> int:
       
        if num < 2:
            return num

        left, right, ans = 1, num // 2, 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= num:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        
        return ans       
object =Solution()
print(object.sqr_root(25))
'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''
            