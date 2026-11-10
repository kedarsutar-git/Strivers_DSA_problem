'''
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Binary Tree:
        3
       / \\
      9  20
        /  \\
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Binary Tree:
          1
         / \\
        2   2
       / \\
      3   3
     / \\
    4   4

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Binary Tree: empty tree

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def height(self,root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    
    def CheckTree(self,root):
        if root is None:
            return True

        leftheight = self.height(root.left)
        rightheight = self.height(root.right)


        if abs(leftheight-rightheight) > 1:
            return False
        
        return (self.CheckTree(root.left) and self.CheckTree(root.right))

        

object = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)

print(object.CheckTree(root))

