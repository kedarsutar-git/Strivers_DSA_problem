'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        heap = []

        for i in range(len(arr)):
            distance = abs(arr[i] - x)

            heap.append((distance, arr[i]))

            # Sort in descending order
            heap.sort(reverse=True)

            if len(heap) > k:
                heap.pop(0)

        ans = []

        for i in range(len(heap)):
            ans.append(heap[i][1])

        ans.sort()

        return ans


object = Solution()

arr = [1, 2, 3, 4, 5]
k = 4
x = 3

print(object.findClosestElements(arr, k, x))

'''
Time complexity: O(n*k*logk)
Space complexity: O(k)  size of the heap

'''