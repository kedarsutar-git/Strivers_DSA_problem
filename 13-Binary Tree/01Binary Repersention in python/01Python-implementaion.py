class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# Creating Node

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)



print(root.data)             # 1
print(root.left.data)        # 2
print(root.right.data)       # 3
print(root.left.left.data)   # 4
print(root.left.right.data)  # 5


'''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None

class Solution:
    def PreorderTraversal(self,root):
        if root is None:
            return []

        return ([root.data] +self.PreorderTraversal(root.left) + self.PreorderTraversal(root.right))

root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)

object  = Solution()
print(object.PreorderTraversal(root))

root  = Node(3)
root.left = Node(4)
root.right = Node(5)


class TreeNode:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def preorderTraversal(self,root):
        if root is None:
            return []

        return ([root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right))


root = TreeNode(23)
root.left = TreeNode(34)
root.right = TreeNode(332)
root.left.left = TreeNode(221)
root.left.right = TreeNode(2)
root.right.left = TreeNode(344)
root.right.right = TreeNode(200)

object = Solution()
print(object.preorderTraversal(root))