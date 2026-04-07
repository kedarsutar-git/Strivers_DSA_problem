'''
Example 1:
nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.



Example 2:
nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.



nums[i-1] < nums[i] > nums[i+1]

peak element is:  nums[i]
'''

# Brute Force method
class Solution:
    def Find_Peak(self,nums:list[int]) ->int:
        for i in range(1,len(nums)-1): 
            if(i==0 or nums[i-1]<nums[i]and i==len(nums)-1 or  nums[i]>nums[i+1]):
                return nums[i]
            
nums = [1,2,3,4,5,6,7,8,5,1]
object = Solution()
print(object.Find_Peak(nums))            

'''
Time Complixity :O(n)
Space Complixity:O(1)

'''


# Optimal method
class solution:
    def FindPeak(self,nums:list[int]) -> int:
        if(len(nums)==1):
            return 0
    
        start = 0
        end = len(nums) -1


        while(start<=end):
            mid = start + (end -start)//2

            if(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return mid
            
            elif(nums[mid]>nums[mid-1]):
                start = mid+1

            elif(nums[mid]>nums[mid+1]):
                end = mid-1

            else:
                start = mid+1    
        return -1


nums = [1,2,3,4,5,6,7,8,9]
object = Solution()
print(object.Find_Peak(nums))
'''
Time complixity :O(logn)
Sapce Comlixity:O(1)
'''            
            
