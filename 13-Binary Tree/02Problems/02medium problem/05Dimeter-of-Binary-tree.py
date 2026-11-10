'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter is the number of edges in the longest path between any two nodes. The path may or may not pass through the root.

Example 1:

Binary Tree:
        1
       / \\
      2   3
     / \\
    4   5

Input: root = [1,2,3,4,5]
Output: 3
Explanation: One longest path is 4 -> 2 -> 1 -> 3.

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def DimeterTree(self,root):
        self.diameter = 0 

        def height(node):
            if node is None:
                return 0

            leftheight = height(node.left)
            rightheight = height(node.right)

            self.diameter = max(self.diameter,leftheight+rightheight)

            return 1 + max(leftheight,rightheight)

        height(root)

        return self.diameter
    

object = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(object.DimeterTree(root))

'''
Time Complexity:O(n**2)
Space Complexity:O(h)

'''

# Optimal method 

