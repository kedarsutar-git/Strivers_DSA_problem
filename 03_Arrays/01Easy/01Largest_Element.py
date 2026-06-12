# Brute Force method 
class Solution:
    def Largest(self,nums:list[int]) -> int:
        largest = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]>largest):
                largest = nums[i]

        return largest
nums = [12,23,45,56,67,78,7823] 
obj = Solution()
print(obj.Largest(nums))   
            
'''
Time Complexity:(n)
Sapce Complexity:(1)
'''            

class Solution:
    def Largest(self,nums:list[int]) ->int:
        Max = 0
        for num in nums:
            Max = max(Max,num)

        return Max
object = Solution()
nums = [12,23,45,56,67,78,7823]
print(object.Largest(nums))



'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 '''


  



