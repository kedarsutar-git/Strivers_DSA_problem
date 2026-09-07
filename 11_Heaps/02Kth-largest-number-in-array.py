'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''

# Better method
class Solution:
    def kthLargestnumber(self,nums:list[int],k:int) ->int:
        heap = []
        for i in range(len(nums)):
            heap.append(nums[i])

            heap.sort()
            heap.reverse()

            if(len(heap)>k):
                heap.pop()

        return heap[-1]

object = Solution()
nums = [3,2,3,1,2,4,5,5,6]
print(object.kthLargestnumber(nums,4))
'''
Time Complexity: O(n*k*logk)
Space Complexity: O(k)  size of the heap
'''


# Optimal method
import heapq
class Solution:
    def kthLargestnumber(self,nums:list[int],k:int) ->int:
        heap = []

        for num in nums:
            heapq.heappush(heap,num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

object = Solution()
nums = [3,2,3,1,2,4,5,5,6]
print(object.kthLargestnumber(nums,4))

'''
Time Complexity: O(nlogk)
Space Complexity: O(k)  size of the heap

'''