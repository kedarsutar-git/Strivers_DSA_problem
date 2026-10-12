'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''

class Solution:
    def slidingWindowMax(self,nums:list[int],k:int) ->list[int]:
        arr = []
        right , left = 0 ,0

        while(right<len(nums)):
            if(right - left + 1<k):
                right += 1

            elif(right - left + 1==k):
                arr.append(max(nums[left:right+1]))

                left += 1
                right += 1

        return arr

object = Solution()
nums =[1,3,-1,-3,5,3,6,7]
print(object.slidingWindowMax(nums,3))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''


# Optimal method 

from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque to store indices of useful elements
        dq = deque()

        # Result list to store window maximums
        result = []

        # Loop through each element
        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Remove all elements from the back that are smaller than current element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index to deque
            dq.append(i)

            # Append max to result once the first window is completed
            if i >= k - 1:
                result.append(nums[dq[0]])

        # Return the result list
        return result


object = Solution()
nums = [1,3,-1,-3,5,3,6,7]
print(object.maxSlidingWindow(nums,3))