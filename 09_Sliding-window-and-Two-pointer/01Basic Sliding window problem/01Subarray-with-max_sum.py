'''
Constant Window: Maximum Sum of Subarray of Size K

Problem Statement: Given an array of integers nums and an integer k, find the 
maximum sum of any contiguous subarray of exactly size k.


Input: nums = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: The possible subarrays of size 3 are [2,1,5] (sum 8),
[1,5,1] (sum 7), [5,1,3] (sum 9),and [1,3,2] (sum 6). The maximum is 9.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

'''


class Solution:
    def SubarraySum(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Sum of first window
        currentSum = sum(nums[:k])
        Max = currentSum

        # Slide the window
        for i in range(k, n):
            currentSum = currentSum + nums[i] - nums[i-k]
            Max = max(Max, currentSum)

        return Max


obj = Solution()
nums = [2, 1, 5, 1, 3, 2]
print(obj.SubarraySum(nums, 3))

'''
Time Complexity :O(n)
space Complexity:O(1)

'''
'''
| Feature          | Sliding Window                                             | Kadane's Algorithm                 |
| ---------------- | ---------------------------------------------------------- | ---------------------------------- |
| Purpose          | Works on a **fixed-size** or **condition-based** window    | Finds the **maximum sum subarray** |
| Window Size      | Usually fixed (`k`) or adjusted with conditions            | Variable, determined automatically |
| Negative Numbers | Doesn't specifically handle negatives                      | Designed to handle negatives       |
| Time Complexity  | O(n)                                                       | O(n)                               |
| Common Problems  | Maximum sum of size `k`, longest substring, minimum window | Maximum subarray sum               |

'''
