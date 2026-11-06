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

