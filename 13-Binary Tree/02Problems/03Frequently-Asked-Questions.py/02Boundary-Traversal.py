'''
Given a root of Binary Tree, perform the boundary traversal of the tree. 

The boundary traversal is the process of visiting the boundary nodes of the binary tree in the anticlockwise direction, starting from the root.

The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

Example 1:

Binary Tree:
          1
         / \\
        2   3
       / \\ / \\
      4  5 6  7
        / \\
       8   9

Input : root = [1, 2, 3, 4, 5, 6, 7, null, null, 8, 9]

Output : [1, 2, 4, 8, 9, 6, 7, 3]

Explanation :



Example 2:

Binary Tree:
          1
         /
        2
       / \\
      4   9
     / \\  /
    6   5 3
         / \\
        7   8

Input : root = [1, 2, null, 4, 9, 6, 5, 3, null, null, null, null, null, 7, 8]

Output : [1, 2, 4, 6, 5, 7, 8]

Explanation :


'''

class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None


class Solution:

    def is_leaf(self,node):
        return (node is not None and node.left is None and node.right is None)

    def add_left_boundary(self,root,boundary):
        current = root.left

        while current is not None:
            if not self.is_leaf(current):
                boundary.append(current.data)

            if current.left is not None:
                current = current.left

            else:
                current = current.right

    def add_leaf_node(self,node,boundary):
        if node is None:
            return

        if self.is_leaf(node):
            boundary.append(node.data)

            return
        
        self.add_leaf_node(node.left,boundary)

        self.add_leaf_node(node.right,boundary)

    def add_right_boundary(self,root,boundary):
        current = root.right
        right_boundary = []

        while current is not None:
            if not self.is_leaf(current):
                right_boundary.append(current.data)

            if current.right is not None:
                current = current.right

            else:
                current = current.left

        for value in reversed(right_boundary):
            boundary.append(value)


    def BoundaryTraversal(self,root):
        if root is None:
            return []

        boundary = []

        if not self.is_leaf(root):
            boundary.append(root.data)

        self.add_left_boundary(root,boundary)

        self.add_leaf_node(root,boundary)

        self.add_right_boundary(root,boundary)


        return boundary


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.left.right = TreeNode(23)
root.right.right  =  TreeNode(2)
object = Solution()

print(object.BoundaryTraversal(root))

