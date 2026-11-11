'''

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Binary Tree:
      1
     / \\
    2   3

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Binary Tree:
        -10
        /  \\
       9   20
          /  \\
         15   7

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi = float('-inf')   # This initializes maxi to the smallest possible value. It’s useful when finding a maximum:
        
        def maxPathDown(node):
            # Base case: if the node is null, return 0
            if node is None:
                return 0
            
            # Ignore negative path sums by comparing with 0
            left_sum = max(0, maxPathDown(node.left))
            right_sum = max(0, maxPathDown(node.right))
            
            # Update the overall maximum path sum (curving through the current node)
            self.maxi = max(self.maxi, left_sum + right_sum + node.val)
            
            # Return the maximum single-branch path sum to the parent node
            return node.val + max(left_sum, right_sum)
        
        maxPathDown(root)   # Call the helper function to start the recursion
        
        return self.maxi   # Return the maximum path sum found during the traversal


root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().maxPathSum(root))  # Output: 42

'''
Time Complexity: O(n), where n is the number of nodes in the binary tree. Each node is visited once.
Space Complexity: O(h), where h is the height of the binary tree. 

This space is used by the recursion stack. In the worst case, the height of the tree can be n (for a skewed tree), leading to O(n) 
space complexity. In a balanced tree, the height would be log(n), leading to O(log(n)) space complexity.

'''
