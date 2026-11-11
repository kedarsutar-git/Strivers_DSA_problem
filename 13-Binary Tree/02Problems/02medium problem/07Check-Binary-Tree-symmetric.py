'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Binary Tree:
        1
       / \\
      2   2
     / \\ / \\
    3  4 4  3

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:

Binary Tree:
        1
       / \\
      2   2
       \\   \\
        3   3

Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''
class TreeNonde:
    def __init__(self,data):
        self.data = data 
        self.left  = None
        self.right = None

class Solution:
    def Symmetric(self,root):
        if root is None:
            return True 

        def helper(left,right):
            if left is None and right is None:
                return True 

            if left is None or right is None:
                return False

            if left.data != right.data:
                return False

            return helper(left.left, right.right) and helper(left.right, right.left)

        return helper(root.left, root.right)

object = Solution()

root = TreeNonde(1)
root.left = TreeNonde(2)
root.right = TreeNonde(2)
root.left.left = TreeNonde(3)
root.right.right = TreeNonde(3)
root.left.right = TreeNonde(5)
root.right.left = TreeNonde(5)
print(object.Symmetric(root))


'''
Time Complexity:O(n)  # where n is the number of nodes in the tree
Space Complexity:O(h)  # where h is the height of the tree

'''
