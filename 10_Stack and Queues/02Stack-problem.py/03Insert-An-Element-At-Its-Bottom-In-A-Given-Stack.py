'''
You are given a stack/deque of integers 'MY-STACK' and an integer ‘X’. Your task is to insert ‘X’ to the bottom of ‘MY-STACK’ and return the updated stack/deque.

Note :
If ‘MY_STACK’ = [7, 1, 4, 5], then the first element represents the element at the bottom of the stack and the last element represents the element at the top of the stack.
For Example :
Let ‘MY_STACK’ = [7, 1, 4, 5] and ‘X’ = 9. So, ‘MY_STACK’ after insertion becomes [9, 7, 1, 4, 5].

Follow Up :
Try to do this without using any other data structure.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= T <=100
1 <= N <= 10^4
0 <= 'X’ and 'MY_STACK[i]’ <= 10^5

Initial Stack                Push(9)                Updated Stack

   Top                                              Top
    ↓                                                ↓
 +-----+                                          +-----+
 |  5  |                                          |  5  |
 +-----+                                          +-----+
 |  4  |                                          |  4  |
 +-----+                                          +-----+
 |  1  |              +-----+                     |  1  |
 +-----+              |  9  |                     +-----+
 |  7  |              +-----+                     |  7  |
 +-----+                 |                        +-----+
    ↑                    |                        |  9  |
 Bottom                  +----------------------> +-----+
                                                    ↑
                                                  Bottom
'''

class Solution:
    def Insert(self, stack: list[int], X: int) -> list[int]:
        temp = []

        while(stack):
            temp.append(stack.pop())

        stack.append(X)

        while(temp):
            stack.append(temp.pop())

        return stack

stack = [1, 2, 3, 4, 5]
object = Solution()
print(object.Insert(stack, 45))

'''
Time Complexity:O(n)
Sapce Complexity:O(n)

'''

