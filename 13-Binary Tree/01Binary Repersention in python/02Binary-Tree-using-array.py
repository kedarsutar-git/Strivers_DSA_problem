'''
          1
        /   \
       2     3
      / \   / \
     4   5 6   7
'''
tree = [1, 2, 3, 4, 5, 6, 7]

# for a node at index i (0 based indexing)

tree = [1, 2, 3, 4, 5, 6, 7]

i = 0

print("Parent:", None)
print("Left:", tree[2 * i + 1])
print("Right:", tree[2 * i + 2])

'''
3. Difference Between Node Representation and Array Representation

Feature              Node Representation       Array Representation
--------------------------------------------------------------------
Storage              Objects/References        List
Memory               Dynamic                   Can waste space
Insertion            Flexible                  Index-based
Best For             General Binary Trees      Complete Binary Trees
LeetCode Usage       Very Common               Less Common
'''


# 