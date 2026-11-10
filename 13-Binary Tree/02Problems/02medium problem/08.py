'''
Given the root of a binary tree, return true if and only if every node’s value is equal to the sum of the values stored in its left and right children.

For any missing ( null ) child, its value is treated as 0.
A leaf node automatically satisfies the rule because both children are null.
Example 1:
Input: root = [1,4,3,5]

Output: false

Explanation:

The root is 1, but its children sum to 4 + 3 = 7. Since 1 ≠ 7, the tree violates the property.
Example 2:
Input: root = [10,4,6,1,3,2,4]

Output: true

Explanation:

4 = 1 + 3
6 = 2 + 4
10 = 4 + 6
All internal nodes satisfy the condition.
'''

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def cheakTree(self,root):
        if root is None:
            return True 

        if root.left is None and root.right is None:
            return True 

        if root.left is not None:   # current node has acctully has left child
            left_val = root.left.data

        else:           # current node has not left child and assign to Zero
            left_val = 0

        if root.right is not None:  # current node has acctully has right child
            right_val = root.right.data

        else:        # current node has not right child and assign to zero
            right_val = 0


        if root.data != left_val + right_val:     # parent node value is equal to sum of left and right child
            return False

        return self.cheakTree(root.left) and self.cheakTree(root.right)

object = Solution()
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(2)

print(object.cheakTree(root))

'''
Time Complexity: O(n) where n is the number of nodes in the tree. We visit each node once.
Space Complexity: O(h) where h is the height of the tree. This space is used

'''