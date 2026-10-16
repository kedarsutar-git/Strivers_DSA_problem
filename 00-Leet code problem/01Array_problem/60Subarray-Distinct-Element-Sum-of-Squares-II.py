'''
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
'''

# Brute force method 

class solution:
    def SubarrSumCount(self,nums:list[int]) ->int:
        all_subarr = []
        count = 0
        Mod = 10**9+7
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                all_subarr.append(nums[i:j])

        for num in all_subarr:
            s = set(num)

            count += len(s)**2

        return count%Mod

nums = [1,2,1]
object = solution()
print(object.SubarrSumCount(nums))

'''
Time Complexity:O(n^2)
Space Complexity:O(n)

'''

# Better method

class solution:
    def SubarrSumCount(self,nums:list[int]) ->int:

        count = 0
        Mod = 10**9+7
        for i in range(len(nums)):
            s = set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                count += len(s)**2
        return count%Mod

nums = [1,2,1]
object = solution()
print(object.SubarrSumCount(nums))

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''

# Optimal method 
from bisect import bisect_right

class Solution:
    def sumCounts(self, nums):
        last = {}  # last occurrence of a value
        index = []  # indices of last occurrences, sorted
        totalsum = curr = ans = 0
        for i, x in enumerate(nums):
            j = last.get(x, -1)
            small = bisect_right(index, j)  # entries <= j (0 if not on last)
            large = len(index) - small  # entries > j
            s = totalsum - sum(index[:small]) if small <= large else sum(index[small:])
            curr += 2 * (s - j * large) + i - j

            if(j >= 0):
                del index[small - 1]  # index[small-1] == j
                totalsum -= j
            index.append(i)
            totalsum += i
            last[x] = i
            ans += curr

        return ans % 1_000_000_007

nums = [1,2,1]
object = Solution()
print(object.sumCounts(nums))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''