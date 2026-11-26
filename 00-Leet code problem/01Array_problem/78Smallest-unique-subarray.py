'''
You are given an integer array nums.

Find the minimum length of a subarray that is not identical to any other subarray in nums.

Return an integer denoting the minimum possible length of such a subarray.

Two subarrays are considered identical if they have the same length and the same elements in corresponding positions.

 

Example 1:

Input: nums = [3,3,3]

Output: 3

Explanation:

Subarrays of length 1: [3] → appears 3 times
Subarrays of length 2: [3, 3] → appears 2 times
Subarrays of length 3: [3, 3, 3] → appears once
The subarray [3, 3, 3] is unique, so the smallest unique subarray length is 3.

Example 2:

Input: nums = [2,1,2,3,3]

Output: 1

Explanation:

Subarrays of length 1:

[2] → appears 2 times
[1] → appears once
[3] → appears 2 times
The subarray [1] is unique, so the smallest unique subarray length is 1.
Example 3:

Input: nums = [1,1,2,2,1]

Output: 2

Explanation:

Subarrays of length 1:

[1] → appears 3 times
[2] → appears 2 times
Subarrays of length 2:

[1, 1] → appears once
[1, 2] → appears once
[2, 2] → appears once
[2, 1] → appears once
There is at least one subarray of length 2 that is unique, so the smallest unique subarray length is 2.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[  i] <= 105
'''



# Brute force method

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        count = 0
        subarr = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                subarr.append(nums[i:j])
                
        for i in range(len(subarr)):
            if subarr.count(subarr[i]) == 1:
                count += 1
                return len(subarr[i])
        
nums = [1,1,2,2,1]
object = Solution()
print(object.smallestUniqueSubarray(nums))  # Output: 2

'''
Time Complexity:O(n**2)
Space Compexity:O(n)

'''



# Genrate Subarray using O(n) Time Complexity

class Solution:
    def Subarray(self,nums:list[int]) ->list[list[int]]:
        subarray = []
        start = 0
        end = 0

        while(end<len(nums)):
            subarray.append(nums[start:end+1])  # Extract the current subarray from start to end
            end += 1

            if end==len(nums): # If end reaches the boundary, advance start and reset end
                start += 1
                end  = start

        return subarray

object = Solution()
nums = [1,2,3,4]

print(object.Subarray(nums))


# Optimal method: O(n log n) time, O(n) space

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base, mod = 100_003, 1_000_000_007
        power = [1] * (n + 1)
        prefix = [0] * (n + 1)

        for i, value in enumerate(nums):
            power[i + 1] = power[i] * base % mod
            prefix[i + 1] = (prefix[i] * base + value) % mod

        def has_unique_subarray(length: int) -> bool:
            frequency = {}
            for left in range(n - length + 1):
                right = left + length
                subarray_hash = (prefix[right] - prefix[left] * power[length]) % mod
                frequency[subarray_hash] = frequency.get(subarray_hash, 0) + 1
            return 1 in frequency.values()

        # If a unique subarray of length k exists, a unique one of length
        # k + 1 also exists (extend it left or right), so binary search works.
        low, high = 1, n
        while low < high:
            middle = (low + high) // 2
            if has_unique_subarray(middle):
                high = middle
            else:
                low = middle + 1
        return low

object = Solution()
nums = [3,3,3]
print(Solution().smallestUniqueSubarray(nums))  

