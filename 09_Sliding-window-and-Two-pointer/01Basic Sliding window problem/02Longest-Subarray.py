'''
Longest Subarray: Longest Subarray with Sum <= K

Problem Statement: Given an array nums and an integer k, return the 
length of the longest contiguous subarray where the sum of its elements 
is less than or equal to k.


Input: nums = [2, 5, 1, 7, 10], k = 14
Output: 3
Explanation: The subarray [2, 5, 1] has a sum of 8 (length 3, valid). Adding the 
next element 7 makes the sum 15 (invalid). The longest valid contiguous subarray is 
[2, 5, 1] with length 3.

Constraints:
1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 10^9
0 <= k <= 10^9
'''

# better method 
class Solution:
    def longestSubarray(self,nums:list[int],k:int) ->int:
        left ,right = 0,0
        Sum = 0
        max_len = 0

        while(right<len(nums)):
            Sum = Sum + nums[right]

            while(Sum>k):
                Sum = Sum - nums[right]
                left +=1

                if(Sum<=k):
                    max_len = max(max_len,right-left+1)
            right +=1

        return max_len 

nums = [2, 5, 1, 7, 10]
object = Solution()
print(object.longestSubarray(nums,14)) 

'''
Time complexity:O(2n)
Space complexity:O(1)

'''

