'''
You are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

The length of the subarray is k, and
All the elements of the subarray are distinct.
Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,5,4,2,9,9,9], k = 3
Output: 15

Explanation: The subarrays of nums with length 3 are:
- [1,5,4] which meets the requirements and has a sum of 10.
- [5,4,2] which meets the requirements and has a sum of 11.
- [4,2,9] which meets the requirements and has a sum of 15.
- [2,9,9] which does not meet the requirements because the element 9 is repeated.
- [9,9,9] which does not meet the requirements because the element 9 is repeated.
We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions



Example 2:

Input: nums = [4,4,4], k = 3
Output: 0

Explanation: The subarrays of nums with length 3 are:
- [4,4,4] which does not meet the requirements because the element 4 is repeated.
We return 0 because no subarrays meet the conditions.
 

Constraints:

1 <= k <= nums.length <= 105
1 <= nums[i] <= 105
'''

class Solution:
    def maxsubarrsum(self,nums:list[int],k:int) ->int:
        right ,left =0 ,0
        maxsum = 0
        currentsum = 0
        count_map ={}

        while(right<len(nums)):

            currentsum += nums[right]

            if nums[right] in count_map:    # use map to count the value of number in the array 
                count_map[nums[right]] += 1

            else:
                count_map[nums[right]] = 1

            if(right-left+1==k): 

                if(len(count_map)==k):

                    maxsum = max(maxsum,currentsum)

                currentsum -= nums[left] 

                count_map[nums[left]] -= 1

                if(count_map[nums[left]]==0):  
                    del count_map[nums[left]]

                left += 1

            right +=1

        return maxsum

object = Solution()
nums = [1,5,4,2,9,9,9]
print(object.maxsubarrsum(nums,3))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''
