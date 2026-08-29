'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
'''

# Brute force method

class Solution:
    def sumSubarrayMins(self,nums:list[int]) ->int:
        mod = int(1e9+7)
        totalsum = 0
        for i in range(len(nums)):
            minnum = nums[i]
            for j in range(i,len(nums)):
                minnum = min(minnum,nums[j])

                totalsum = (totalsum + minnum)%mod

        return totalsum
object = Solution()
nums = [11,81,94,43,3]
print(object.sumSubarrayMins(nums))

'''
Time Complexity:O(n^2)
Space Complexity:O(1)

'''

# optimal method 


class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)

        # Next Smaller Element
        nse = [n] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nse[i] = stack[-1]

            stack.append(i)

        # Previous Smaller or Equal Element
        psee = [-1] * n
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                psee[i] = stack[-1]

            stack.append(i)

        # Calculate answer
        MOD = 10**9 + 7
        total = 0

        for i in range(n):
            left = i - psee[i]
            right = nse[i] - i

            contribution = arr[i] * left * right

            total = (total + contribution) % MOD

        return total

object = Solution()
arr  =[11,81,94,43,3]
print(object.sumSubarrayMins(arr))