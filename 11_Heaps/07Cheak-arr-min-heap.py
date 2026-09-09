'''
Check if an array represents a min heap


3

Problem Statement: Given an array of integers nums. Check whether the array represents a binary min-heap or not. Return true if it does, otherwise return false.
A binary min-heap is a complete binary tree where the key at the root is the minimum among all keys present in a binary min-heap and the same property is recursively true for all nodes in a Binary Tree.

Examples
Input: nums = [10, 20, 30, 21, 23]
Output: true
Explanation: Each node has a lower or equal value than its children.


Input: nums = [10, 20, 30, 25, 15]
Output: false
Explanation: The node with value 20 has a child with value 15, thus it is not a min-heap.
'''

class Solution:
    # Function to check if the given array is a min-heap
    def isMinHeap(self, nums):
        n = len(nums)

        # Iterate through all non-leaf nodes
        for i in range(n // 2):

            # Calculate left child index
            left = 2 * i + 1

            # If left child exists and is smaller than parent, not a min-heap
            if(left < n and nums[i] > nums[left]):
                return False

            # Calculate right child index
            right = 2 * i + 2

            # If right child exists and is smaller than parent, not a min-heap
            if(right < n and nums[i] > nums[right]):
                return False

        # If no violations found, it is a min-heap
        return True

object = Solution()
nums = [10, 20, 30, 21, 23]
print(object.isMinHeap(nums))  

'''
Time Complexity: O(n)
Space Complexity: O(1)

'''