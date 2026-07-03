'''
Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].


Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].


Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

class Solution:
    def TwoSum(self,nums:list[int],tar:int) ->list[int]:
        start = 0
        end = len(nums)-1

        while(start<end):
            if(nums[start]+nums[end]==tar):
                return [start+1,end+1]
            
            elif(nums[start]+nums[end]>tar):
                end -=1

            else:
                start+=1

        return [-1,-1]

nums =  [2,7,11,15]
object = Solution()
print(object.TwoSum(nums,9))              

'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
'''

class Solution:
    def PowerOfFour(self,n:int) ->bool:

        if(n<=0):
            return False
        
        start = 0
        end = int(n**0.5)

        while(start<=end):
            mid = start+(end-start)//2

            if(4**mid==n):
                return True 
            
            elif(4**mid>n):
                end = mid-1

            else:
                start = mid+1

        return False

object = Solution()
print(object.PowerOfFour(16))




'''
You are given an integer array height of length n. There are n vertical
lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.



Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by 
array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
the container can contain is 49.


Example 2:
Input: height = [1,1]
Output: 1
'''

class Solution:
    def MaxWater(self,nums:list) ->int:
        start = 0
        end = len(nums)-1

        Max = 0

        while(start<end):
            width = end-start

            Area = width*min(nums[start],nums[end])
            
            Max = max(Max,Area)

            if(nums[start]<nums[end]):
                start+=1

            elif(nums[start]>nums[end]):
                end-=1

            else:
                start+=1

        return Max
            
nums=[1,8,6,2,5,4,8,3,7]
object = Solution()
print(object.MaxWater(nums))