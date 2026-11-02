'''
Given a binary tree with root node. Return the In-order,Pre-order and Post-order traversal of the binary tree.

Example 1:
Input : root = [1, 3, 4, 5, 2, 7, 6 ]

Output : [ [5, 3, 2, 1, 7, 4, 6] , [1, 3, 5, 2, 4, 7, 6] , [5, 2, 3, 7, 6, 4, 1] ]

Explanation : The In-order traversal is [5, 3, 2, 1, 7, 4, 6].

The Pre-order traversal is [1, 3, 5, 2, 4, 7, 6].

The Post-order traversal is [5, 2, 3, 7, 6, 4, 1].



Example 2:
Input : root = [1, 2, 3, null, null, null, 6 ]

Output : [ [2, 1, 3, 6] , [1, 2, 3, 6] , [2, 6, 3, 1] ]

Explanation : The In-order traversal is [2, 1, 3, 6].

The Pre-order traversal is [1, 2, 3, 6].

The Post-order traversal is [2, 6, 3, 1].



Now Your Turn!
Pick the correct output for the given input
Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]


[ [5, 1, 8, 6, 2, 4, 5], [8, 6, 1, 5, 4, 2, 5], [6, 8, 1, 4, 5, 2, 5] ]

[ [8, 6, 1, 5, 4, 2, 5], [5, 1, 8, 6, 2, 4, 5], [6, 8, 1, 4, 5, 2, 5] ]

[ [8, 6, 1, 5, 4, 2, 5], [6, 8, 1, 4, 5, 2, 5], [5, 1, 8, 6, 2, 4, 5] ]

[ [5, 1, 8, 6, 2, 4, 5], [6, 8, 1, 4, 5, 2, 5], [8, 6, 1, 5, 4, 2, 5] ]
Still unsure what the problem is asking ?

Let’s go through a few more examples, step by step, to make it clearer.

Constraints:
1 <= Number of Nodes <= 105
0 <= Node.val <= 105
'''

class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Solution:
    def Inorder(self,root):
        if root is None:
            return []

        return self.Inorder(root.left) + [root.data] + self.Inorder(root.right)

    def Preorder(self,root):
        if root is None:
            return []

        return [root.data] + self.Preorder(root.left) + self.Preorder(root.right)

    def Postorder(self,root):
        if root is None:
            return []

        return self.Postorder(root.left) + self.Postorder(root.right) + [root.data]

    def tree_traversal(self,root):
        return [self.Inorder(root),self.Preorder(root),self.Postorder(root)]


object = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right  = TreeNode(7)

print(object.tree_traversal(root))
