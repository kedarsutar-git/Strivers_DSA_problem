class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def levelorder(self,root) -> list[list[int]]:
        if root is None:
            return []

        q = []
        res = []
        q.append(root)
        current_level = 0
        while q:
            len_q = len(q)
            res.append([])
            for _ in range(len(q)):
                node = q.pop(0)
                res[current_level].append(node.data)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            current_level += 1

        return res

object = Solution()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

object = Solution()
print(object.levelorder(root))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''
diagram = """

STEP 01: Add the root node to the Queue.

                         5

Queue: [5]


STEP 02: Pop 5 and add its left child (12) and right child (13).

                         5
                       /   \\
                     12     13

Traversal Order: 5
Queue: [12, 13]


STEP 03: Pop 12 and add its left child (7).

                         5
                       /   \\
                     12     13
                    /
                   7

Traversal Order: 5 -> 12
Queue: [13, 7]


STEP 04: Pop 13 and add its left child (14) and right child (2).

                         5
                       /   \\
                     12     13
                    /      /  \\
                   7      14    2

Traversal Order: 5 -> 12 -> 13
Queue: [7, 14, 2]


STEP 05: Pop 7 and add its left child (17) and right child (23).

                         5
                       /   \\
                     12     13
                    /      /  \\
                   7      14    2
                  / \\
                17  23

Traversal Order: 5 -> 12 -> 13 -> 7
Queue: [14, 2, 17, 23]


STEP 06: Pop 14 and add its left child (27) and right child (3).

                         5
                       /   \\
                     12     13
                    /      /  \\
                   7      14    2
                  / \\    / \\
                17  23  27  3

Traversal Order: 5 -> 12 -> 13 -> 7 -> 14
Queue: [2, 17, 23, 27, 3]


STEP 07: Pop 2 and add its left child (8) and right child (11).

                         5
                       /   \\
                     12     13
                    /      /  \\
                   7      14    2
                  / \\    / \\  / \\
                17  23  27  3  8  11

Traversal Order: 5 -> 12 -> 13 -> 7 -> 14 -> 2
Queue: [17, 23, 27, 3, 8, 11]


STEP 08: Pop the remaining nodes until the Queue becomes empty.

                         5
                       /   \\
                     12     13
                    /      /  \\
                   7      14    2
                  / \\    / \\  / \\
                17  23  27  3  8  11

Traversal Order:
5 -> 12 -> 13 -> 7 -> 14 -> 2 -> 17 -> 23 -> 27 -> 3 -> 8 -> 11

Queue: []

"""
print(diagram)

