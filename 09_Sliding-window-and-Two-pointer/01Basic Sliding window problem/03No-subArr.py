'''
Problem Statement
Given an array of integers nums and an integer k, return the total number of 
continuous subarrays whose sum equals to k.


Example 1:

Input: nums = [1, 1, 1], k = 2
Output: 2
Explanation: The subarrays are [1, 1] (starting at index 0) and [1, 1] 
(starting at index 1).


Example 2:

Input: nums = [1, 2, 3], k = 3
Output: 2
Explanation: The subarrays are [1, 2] and [3].

Explanation:
As mentioned in the video, this is a Pattern 3 problem. Because the condition is constant (sum exactly equals 
), it is often difficult to use a simple sliding window because negative numbers can make the sum non-monotonic.

Approximation Strategy: One effective approach to solve this is to treat it as finding the count of subarrays where
sum <= k and subtracting the count of subarrays where sum <= k - 1.
Standard Approach: While the video explains the logic behind this pattern, most standard implementations for this 
specific problem on competitive platforms use a Prefix Sum with a Hash Map to achieve 
time complexity, rather than a sliding window, due to the presence of potential negative numbers in the array.


Constraints
1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
'''

class Solution:
        def subarrsum(self,nums:list[int],k:int):

            def subArr1(nums):
                current_sum = 0
                left = 0
                right = 0
                count = 0

                while(right<len(nums)):
                    current_sum = current_sum + nums[right]

                    while(current_sum>k and left<=right):
                        current_sum = current_sum-nums[right]

                        left +=1

                    count += (right-left+1)
                    right += 1
                return count

            def subArr2(nums):
                current_sum = 0
                left = 0
                right = 0
                count = 0

                while(right<len(nums)):
                    current_sum = current_sum + nums[right]

                    while(current_sum>k-1 and left<=right):
                        current_sum = current_sum-nums[right]

                        left +=1

                    count += (right-left+1)
                    right += 1
                return count
    
            x = subArr1(nums)
            y = subArr2(nums)

            return  x - y   
nums = [1, 1 , 1]
object = Solution()
print(object.subarrsum(nums,2))    

'''
Time Complexity:O()
Space Complexity:O(1)
'''
   
    

