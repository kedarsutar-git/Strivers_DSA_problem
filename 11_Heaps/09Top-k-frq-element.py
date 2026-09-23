'''
Given an integer array nums and an integer k, return any order list of the k most frequent elements in nums.

Your solution must run in better than O(n log n) time, where n = nums.length.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears once.

       The two most-frequent elements are 1 and 2.

Example 2:
Input: nums = [4,4,6,6,7], k = 2

Output: [4,6]

Explanation: 4 and 6 both occur twice (highest), 7 occurs once.
'''
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frq = {}
        for num in nums:
            if num in frq:
                frq[num] += 1
            else:
                frq[num] = 1

        arr = []
        for key,value in frq.items():
            arr.append([value,key])

        arr.sort(reverse=True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])

        return ans 
        
nums =[1,2,1,2,1,2,3,1,3,2]
k = 2
object = Solution()
print(object.topKFrequent(nums, k))

'''
Time Complexity:O(n)
Space Complexity:O(n)

'''
