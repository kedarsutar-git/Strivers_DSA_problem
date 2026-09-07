
'''
Given an integer array arr[] and an integer k, find and return the kth smallest element in the given array.
Note: The kth smallest element is determined based on the sorted order of the array.

Examples :

Input: arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
Output: 5
Explanation: 4th smallest element in the given array is 5.


Input: arr = [7, 10, 4, 3, 20, 15], k = 3
Output: 7
Explanation: 3rd smallest element in the given array is 7.


Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105
1 ≤ k ≤  arr.size() 
'''
class Solution:
    def kthSmallest(self,nums:list[int],k:int) ->int:
        heap = []
        for i in range(len(nums)):
            heap.append(nums[i])
            heap.sort()    # O(logk)

            if len(heap) > k:
                heap.pop()

        return heap[-1]

nums = [7,10,4,3,20,15]
object = Solution()
print(object.kthSmallest(nums,3))

'''
Time Complexity: O(nlogk) 
Space Complexity: O(k)  size of the heap 
'''