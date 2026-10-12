'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
 

Follow-up: Could you find a solution with O(n) time complexity?
'''

class Solution:
    def sumSubarr(self,nums:list[int]) ->int:
        totalsum = 0
        for i in range(len(nums)):
            minnum,maxnum = nums[i],nums[i]
            for j in range(i,len(nums)):
                minnum = min(minnum,nums[j])
                maxnum = max(maxnum,nums[j])

                totalsum += (maxnum-minnum)

        return totalsum

object = Solution()
nums =[4,-2,-3,4,1]
print(object.sumSubarr(nums))


'''
Time Complexity:O(n^2)
Space Complexity:O(1)
'''


# Optimal method


class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)

        # --------------------------------
        # Next Smaller Element
        # --------------------------------
        def findNSE():
            nse = [n] * n
            stack = []

            for i in range(n - 1, -1, -1):

                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]

                stack.append(i)

            return nse

        # --------------------------------
        # Previous Smaller or Equal
        # --------------------------------
        def findPSEE():
            psee = [-1] * n
            stack = []

            for i in range(n):

                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()

                if stack:
                    psee[i] = stack[-1]

                stack.append(i)

            return psee

        # --------------------------------
        # Next Greater Element
        # --------------------------------
        def findNGE():
            nge = [n] * n
            stack = []

            for i in range(n - 1, -1, -1):

                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()

                if stack:
                    nge[i] = stack[-1]

                stack.append(i)

            return nge

        # --------------------------------
        # Previous Greater or Equal
        # --------------------------------
        def findPGEE():
            pgee = [-1] * n
            stack = []

            for i in range(n):

                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()

                if stack:
                    pgee[i] = stack[-1]

                stack.append(i)

            return pgee

        # Find all required indices
        nse = findNSE()
        psee = findPSEE()

        nge = findNGE()
        pgee = findPGEE()

        # --------------------------------
        # Calculate maximum contribution
        # --------------------------------
        max_sum = 0

        for i in range(n):

            left = i - pgee[i]
            right = nge[i] - i

            count = left * right

            max_sum += nums[i] * count

        # --------------------------------
        # Calculate minimum contribution
        # --------------------------------
        min_sum = 0

        for i in range(n):

            left = i - psee[i]
            right = nse[i] - i

            count = left * right

            min_sum += nums[i] * count

        # Range = Maximum - Minimum
        return max_sum - min_sum


object = Solution()

nums = [4,-2,-3,4,1]

print(object.subArrayRanges(nums))