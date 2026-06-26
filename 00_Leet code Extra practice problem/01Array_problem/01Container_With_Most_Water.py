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

# Brute force method

class Solution:
    def MaxWater(self,nums:list[int]) ->int:
        Max_area = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                width = j-i
                current_area = width * min(nums[i],nums[j])

                Max_area = max(Max_area,current_area)

        return Max_area

nums =  [1,8,6,2,5,4,8,3,7]
object = Solution()
print(object.MaxWater(nums))

'''
Time Complexity:O(n**2)
Space Complexity:O(1)
'''

# optimal method

class Solution:
    def MaxWater(self,nums:list[int]) ->int:
        Max_area = 0
        left = 0
        right = len(nums)-1
        while(left<right):
            width = right-left
            current_area = width*min(nums[left],nums[right])

            Max_area = max(Max_area,current_area)

            if(nums[left]<nums[right]):
                left +=1

            elif(nums[left]>nums[right]):
                right -=1

            else:      # nums[left]==nums[right]
                left +=1

        return Max_area

nums = [1,8,6,2,5,4,8,3,7]    
object = Solution()
print(object.MaxWater(nums))

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''




