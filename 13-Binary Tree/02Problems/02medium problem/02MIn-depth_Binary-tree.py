'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Binary Tree:
        3
       / \\
      9  20
        /  \\
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Binary Tree:
    2
     \\
      3
       \\
        4
         \\
          5
           \\
            6

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def MinDepth(self,root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return 1 + self.MinDepth(root.right)

        if root.right is None:
            return 1 + self.MinDepth(root.left)

        leftDepth = self.MinDepth(root.left)
        rightDepth = self.MinDepth(root.right)

        return 1 + min(leftDepth,rightDepth)

object = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(90)
print(object.MinDepth(root))
'''
Time Complexity:O(n)
Space Complexity:O(h)   # h is the height of the tree
'''


