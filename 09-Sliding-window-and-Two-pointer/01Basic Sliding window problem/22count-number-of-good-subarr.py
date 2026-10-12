'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.
Example 2:

Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 109
'''

class Solution:
    def countGoodsubarr(self,nums:list[int],k:int):
        right,left = 0 ,0
        count_map = {}
        count,pairscount = 0,0

        while(right<len(nums)):
            if nums[right] in count_map:
                pairscount += count_map[nums[right]]

                count_map[nums[right]] += 1


            else:
                count_map[nums[right]] = 1

            while(pairscount>=k):
                count_map[nums[left]] -=1
                pairscount -= count_map[nums[left]]
                left += 1

            count += left

            right += 1
        return count

nums = [3,1,4,3,2,2,4]
object = Solution()
print(object.countGoodsubarr(nums,2))

'''
Time Complexity:O(n)
Sapce Complexity:O(n)

'''