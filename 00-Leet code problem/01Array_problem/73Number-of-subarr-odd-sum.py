'''
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input:
arr = [1, 3, 5]

Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input:
arr = [2, 4, 6]

Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input:
arr = [1, 2, 3, 4, 5, 6, 7]

Output: 16
 

Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
'''

# Brute force method

class Solution:
    def CountSubarr(self,nums:list[int]) ->int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums) + 1):
                if sum(nums[i:j])%2 != 0:
                    count += 1

        return count

object = Solution()
nums = [1, 3, 5]
print(object.CountSubarr(nums))


'''
Time Complexity:O(n**2)
Space Complexity:O(1)

'''

# Optimal method

class Solution:
    def CountSubarrSumodd(self,nums:list[int]) ->int:
        ans = 0
        even = 0
        odd = 0
        MOD = 10**9 + 7
        for num in nums:
            if num%2==0:
                even += 1

            else:
                odd, even = even + 1, odd

            ans = (ans+odd)%MOD

        return ans  

object = Solution()
nums =  [1, 3, 5]
print(object.CountSubarrSumodd(nums))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''