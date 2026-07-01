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
    def Sqr_root(self,num:int) ->int:
        
        start = 1
        end = int(num**0.5)
        ans = 1
        while(start<=end):
            mid = start + (end - start)//2

            if(mid*mid<=num):
                ans = mid

                start = mid + 1

            else:
                end = mid - 1

        return ans 

object = Solution()
print(object.Sqr_root(56))    
'''
Time Complexity:O(logn)
Space Complexity:O(1)
'''
            


                    