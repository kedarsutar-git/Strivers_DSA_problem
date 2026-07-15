'''
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

 

Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].


Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

Constraints:  

1 <= nums.length <= 1000
1 <= nums[i] <= 2000
'''

# Brute force method
class Solution:
    def countSubarr(self,nums:list[int]) ->int:
        count_map1 = {}
        for num in nums:
            if(num in count_map1):
                count_map1[num] += 1

            else:
                count_map1[num] = 1

        countsubarr = 0
        for i in range(len(nums)):
            count_map2 = {}
            for j in range(i,len(nums)):
                if(nums[j] in count_map2):
                    count_map2[nums[j]] += 1

                else:
                    count_map2[nums[j]] = 1


                if(len(count_map1)==len(count_map2)):
                    countsubarr += 1

        return countsubarr

nums = [5,5,5,5]
object = Solution()
print(object.countSubarr(nums)) 

'''
Time Compleixty:O(n**2)
Space Complexity:O(n+n)
'''


# Optimal method
#  
class Solution:
    def countSubarr(self, nums: list[int]) -> int:

        totalDistinct = len(set(nums))

        left = 0
        right = 0
        count = 0
        freq = {}

        while right < len(nums):

            if nums[right] in freq:
                freq[nums[right]] += 1
            else:
                freq[nums[right]] = 1

            while len(freq) == totalDistinct:

                # Every subarray starting at 'left' and ending at
                # right, right+1, ..., n-1 will remain complete.
                count += len(nums) - right

                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            right += 1

        return count


# Driver Code
nums = [1, 3, 1, 2, 2]

obj = Solution()
print(obj.countSubarr(nums))       


'''
Time Compleixty:O(n)
Space Complexity:O(n)
'''