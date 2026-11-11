# Def for a Binary tree node

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        if root is None:
            return []

        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))


object = Solution()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(object.preorderTraversal(root))  # [1, 2, 4, 5, 3, 6, 7]

# Tree str :

'''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
'''


'''
[root.val] → Current root node.

preorderTraversal(root.left) → Left subtree.

preorderTraversal(root.right) → Right subtree.



The three parts return:

[root.val]                         # [1]

self.preorderTraversal(root.left)  # [2, 4, 5]

self.preorderTraversal(root.right) # [3, 6, 7]

'''





