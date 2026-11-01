'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def Inorder(self,root):
        if root is None:
            return []

        return (self.Inorder(root.left) + [root.data] + self.Inorder(root.right))

object = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

print(object.Inorder(root))

'''
Time Complexity:O(n**2)
Space Complexity:O(1)
'''