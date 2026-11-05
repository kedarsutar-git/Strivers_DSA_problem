class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def SameTree(self, p, q):
        # Both nodes are empty, so this part of both trees matches.
        if p is None and q is None:
            return True

        # Only one node is empty, so the tree structures differ.
        if p is None or q is None:
            return False

        # Values and both corresponding subtrees must match.
        return (p.data == q.data and self.SameTree(p.left, q.left) and self.SameTree(p.right, q.right))

object = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(object.SameTree(root1, root2))  # Output: True


'''
Time Complexity:O(n)
Space Complexity:O(h)
            
'''

