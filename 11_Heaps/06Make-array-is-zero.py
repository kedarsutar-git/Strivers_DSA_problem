'''
You are given a non-negative integer array nums. In one operation, you must:

Choose a positive integer x such that x is less than or equal to the smallest non-zero element in nums.
Subtract x from every positive element in nums.
Return the minimum number of operations to make every element in nums equal to 0.

 

Example 1:

Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
Example 2:

Input: nums = [0]
Output: 0
Explanation: Each element in nums is already 0 so no operations are needed.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
class Solution:
    def minoperations(self,nums:list[int]) ->int:
        opertions = 0
        while(sum(nums)!=0):
            for value in nums:
                if(value>0):
                    minnum = value
                    break
           
            for i in range(len(nums)):
                if(nums[i]>0):
                    minnum = min(minnum,nums[i])

            for i in range(len(nums)):
                if(nums[i]>0):
                    nums[i]-=minnum

            opertions+=1
        return opertions
object = Solution()
nums =[1,5,0,3,5]
print(object.minoperations(nums))

'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

# Optimal method (using heap)

import heapq

class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        heap = []

        for value in nums:
            if value > 0:
                heapq.heappush(heap, value)

        operation = 0
        previous = 0

        while heap:
            value = heapq.heappop(heap)

            if value != previous:
                operation += 1
                previous = value

        return operation

object = Solution()
nums = [1, 5, 0, 3, 5]
print(object.minimumOperations(nums))

'''
Time Complexity: O(n log n)
Space Complexity: O(n)
'''