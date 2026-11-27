'''
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.

 

Example 1:

Input:
nums = [1, 4, 25, 10, 25]
k = 2

Output: 5
Explanation: The two unique positive integers that do not appear in nums which we append are 2 and 3.
The resulting sum of nums is 1 + 4 + 25 + 10 + 25 + 2 + 3 = 70, which is the minimum.
The sum of the two integers appended is 2 + 3 = 5, so we return 5.
Example 2:

Input:
nums = [5, 6]
k = 6

Output: 25
Explanation: The six unique positive integers that do not appear in nums which we append are 1, 2, 3, 4, 7, and 8.
The resulting sum of nums is 5 + 6 + 1 + 2 + 3 + 4 + 7 + 8 = 36, which is the minimum. 
The sum of the six integers appended is 1 + 2 + 3 + 4 + 7 + 8 = 25, so we return 25.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 108
'''

class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)
        
        count = 0
        curr = 1
        ans = 0
        while(count<k):
            if curr not in nums:
                ans += curr
                count += 1
            curr += 1
        return ans
    
nums = [1]
object = Solution()
print(object.minimalKSum(nums,100000000))

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''



# Optimal method 

class Solution:
    def minmalKsum(self,nums: list[int], k: int) ->int:
        nums.sort()
        total = 0
        prev = 0
        for num in nums:
            if num ==prev:
                continue

            missing = num - prev - 1

            if missing>0:
                take = min(k,missing)
                total += (prev+1+prev+take) * take//2
                k -= take

                if k==0:
                    return total

            prev = num

        total += (prev + 1 + prev + k) *k//2
        return total

    
nums = [1]
object = Solution()
print(object.minmalKsum(nums,100000000))


