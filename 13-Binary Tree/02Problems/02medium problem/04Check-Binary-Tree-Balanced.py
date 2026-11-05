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

