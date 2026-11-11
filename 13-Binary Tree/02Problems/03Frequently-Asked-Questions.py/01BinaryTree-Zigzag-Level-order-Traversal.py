'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Binary Tree:
        3
       / \\
      9  20
        /  \\
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Binary Tree:
    1

Input: root = [1]
Output: [[1]]
Example 3:

Binary Tree: empty tree

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None

class Solution:
    def ZigzagTraversal(self,root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [[root.data]]

        q = []
        res = []
        q.append(root)

        left_to_right = True

        while q:
            len_q = len(q)
            row = [0]*len_q

            for i in range(len_q):
                node = q.pop(0)

                if left_to_right:
                    index = i

                else:
                    index = len_q - 1 - i

                row[index] = node.data 

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            res.append(row)

            if left_to_right:
                left_to_right = False

            else:
                left_to_right = True
                
        return res
    
object = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(object.ZigzagTraversal(root))
