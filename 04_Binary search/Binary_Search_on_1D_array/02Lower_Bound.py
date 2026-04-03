'''
what is lower Bound :
Smallest index such that arr[index] >= x
x = input number 

EX.1:
arr = [3,5,8,15,19] , n = 5

x = 8
arr[index] >= x
arr[2] >= 8

output is : 2

EX.2:
x = 9
arr[index] >= x
arr[3] >= 9

output is : 3

EX.3
x = 16

arr[index]>= x
arr[4] >= 16

output is : 4

EX.3:
x =20(x = 20 are not present is the arr)

arr[index]>=x
arr[n] >=20

output is : n = 5


arr = [3,5,8,15,19,19,19] n = 7

x = 19
arr[index] >= x

arr[4] >= 19

output is:4 (minmum index not 5 and 6)


'''
# Brute Force method
class Solution:
    def LowerBound(self,nums:list[int],x:int) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if(nums[i]>=x):
                return i
        return n   

nums = [3,5,8,15,19]
object = Solution()
print(object.LowerBound(nums,16))                
        
'''
Time Complixity :O(n)
Space Complixity :O(1)
'''    

# Optimal method (using Binary search)

class Solution:
    def LowerBound(self,nums:list[int],x) -> int:
        start  = 0
        end = len(nums) -1

        while(start<=end):
            mid = start +(end-start)//2

            if(nums[mid]>=x):
                return mid
                end = mid-1

            else:
                start = mid+1

        return len(nums)

nums = [1,2,3,3,5,8,8,10,10,11]

object = Solution()
print(object.LowerBound(nums,22))
'''
Time Complixity:O(nlogn)
Space Complixity :O(1)
'''







