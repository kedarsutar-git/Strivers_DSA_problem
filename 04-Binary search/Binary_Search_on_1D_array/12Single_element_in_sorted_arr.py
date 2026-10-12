'''
Example 1:
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2


Example 2:
Input: nums = [3,3,7,7,10,11,11]
Output: 10
'''

# Brute force method

class Solution:
    def Single_element(Self,nums:list[int]) -> int:
        for i in range(1,len(nums)-1):
            if(nums[i-1]!=nums[i]!=nums[i+1]):
                return nums[i]
            
nums = [3,3,7,7,10,11,11]   
object = Solution()
print(object.Single_element(nums))        

'''
Time Complixity:O(n)
Space Complixity:O(1)

'''

# Optimal method

class Solution:
    def Find_single_element(self,nums:list[int]) ->int:
       
        if(len(nums)==1):
            return nums[0]
        
        if(nums[0]!=nums[1]):
            return nums[0]
        
        if(nums[len(nums)-1]!=nums[len(nums)-2]):
            return nums[len(nums)-1]
        
        start = 1
        end = len(nums) - 2
        while(start<=end):
            mid = start+(end-start)//2
            if(nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]):
                return nums[mid]
            
            if(mid%2==1 and nums[mid-1]==nums[mid] or mid%2==0 and nums[mid+1]==nums[mid]):
                start = mid+1

            else:
                end = mid-1
 
        return -1

nums = [3,3,7,7,10,11,11]   
object = Solution()
print(object.Find_single_element(nums))          

'''
Time Complixity:O(logn)
Space Complixity:O(1)
'''
            