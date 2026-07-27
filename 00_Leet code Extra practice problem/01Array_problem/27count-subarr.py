'''
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''

# Brute force method 
class Solution:
    def countSubarr(self,nums:list[int],k:int) ->int:
        maxnum = max(nums)
        count = 0

        for i in range(len(nums)):
            count_map = {}
            for j in range(i,len(nums)):

                if nums[j] in count_map:
                    count_map[nums[j]] +=1

                else:
                    count_map[nums[j]] = 1

                if(count_map.get(maxnum,0)>=k):
                    count +=1

        return count

object = Solution()
nums = [1,3,2,3,3]
print(object.countSubarr(nums,2))

'''
Time Complexity:O(n^2)
Sapce Complexity:O(n)

'''

# Optimal method 
class Solution:
    def countsubarr(self,nums:list[int],k:int) ->int:
        right,left = 0,0
        count = 0
        count_map = {}
        maxnum = max(nums)
        while(right<len(nums)):
            if nums[right] in count_map:
                count_map[nums[right]] +=1

            else:
                count_map[nums[right]] = 1

            while(count_map.get(maxnum,0)>=k):
                count +=len(nums)-right

                count_map[nums[left]] -=1

                if(count_map[nums[left]]==0):
                    del count_map[nums[left]]

                left +=1
            right+=1

        return count

nums = [1,3,2,3,3]

object = Solution()
print(object.countsubarr(nums,2))            

'''
Time Complexity:O(n)
Sapce Complexity:O(1)

'''