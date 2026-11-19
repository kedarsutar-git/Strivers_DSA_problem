'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Binary Tree:
        3
       / \\
      9  20
        /  \\
       15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
Example 2:


Binary Tree:
          1
         / \\
        2   3
       / \\ / \\
      4  5 6  7

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
Column -2: Only node 4 is in this column.
Column -1: Only node 2 is in this column.
Column 0: Nodes 1, 5, and 6 are in this column.
          1 is at the top, so it comes first.
          5 and 6 are at the same position (2, 0), so we order them by their value, 5 before 6.
Column 1: Only node 3 is in this column.
Column 2: Only node 7 is in this column.
Example 3:


Binary Tree:
          1
         / \\
        2   3
       / \\ / \\
      4  6 5  7

Input: root = [1,2,3,4,6,5,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation:
This case is the exact same as example 2, but with nodes 5 and 6 swapped.
Note that the solution remains the same since 5 and 6 are in the same location and should be ordered by their values.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
0 <= Node.val <= 1000
'''
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def DFS(self,node,row,column,nodes):
        if node is None:
            return 

        # Store one tuple so the list can sort by column, row, and value.
        nodes.append((column, row, node.data))

        # Moving left increases the row and decreases the columns

        self.DFS(node.left,row+1,column-1,nodes)

        # Moving right increases the row and increases the columns

        self.DFS(node.right,row+1,column+1,nodes)

        # returns nodes groups by vertical
        # columns from left to right 

    def Vertical_traversal(self,root):
        if root is None:
            return []

        nodes = []

        self.DFS(root,0,0,nodes)

        # tuple sorting follows column then row then value

        nodes.sort()

        answer = []

        pre_column = None

        # A new group is started whenever
        # The clumn changes

        for column, row, data in nodes:
            if pre_column is None or column != pre_column:
                answer.append([])
                pre_column = column

            answer[-1].append(data)

        return answer

object  = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
root.right.left = TreeNode(45)
root.right.right = TreeNode(89)

print(object.Vertical_traversal(root))


'''
Time Complexity:O(nlogn)
Space Complexity:O(n)
'''
