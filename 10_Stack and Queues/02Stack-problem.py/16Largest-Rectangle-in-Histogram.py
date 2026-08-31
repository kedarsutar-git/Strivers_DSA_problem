'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
'''
# Brute force method

class Solution:
    def  largestRectangleArea(self,nums:list[int]) ->int:
        maxarea = 0
        for i in range(len(nums)):    # For starting indices
            min_height = float("inf")
            for j in range(i,len(nums)):   # For ending indices
                min_height = min(min_height,nums[j])  # update the min_height 

                width = j - i + 1        # Find the width  
                area = min_height * width   # Find the Area 

                maxarea = max(maxarea,area)   # Update the maxarea 

        return maxarea

object = Solution()
nums = [2,1,5,6,2,3]
print(object.largestRectangleArea(nums))

'''
Time Complexity:O(n^2)
Space Complexity:O(1)
'''




class Solution:
    def largestRectangleArea(self, nums: list[int]) -> int:

        def findNSE():
            n = len(nums)
            nse = [n] * n
            stack = []

            for i in range(n - 1, -1, -1):

                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]

                stack.append(i)

            return nse

        def findPSEE():
            n = len(nums)
            psee = [-1] * n
            stack = []

            for i in range(n):

                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()

                if stack:
                    psee[i] = stack[-1]

                stack.append(i)

            return psee

        NSE = findNSE()
        PSEE = findPSEE()

        maxnum = 0

        for i in range(len(nums)):
            area = nums[i] * (NSE[i] - PSEE[i] - 1)
            maxnum = max(maxnum, area)

        return maxnum


object = Solution()

nums = [2, 1, 5, 6, 2, 3]

print(object.largestRectangleArea(nums))