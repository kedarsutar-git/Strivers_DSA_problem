'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        current = head
        arr = []
        while(current is not None):
            arr.append(current.val)

            current = current.next

        i = left - 1

        j = right - 1

        while(i<j):
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1

        current = head
        k = 0 
        while(current is not None):
            current.val  = arr[k]
            current = current.next
            k += 1

        return head
    
            

# Build list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
result = sol.reverseBetween(head, 2, 4)

# Print result
while result:
    print(result.val, end="->")
    result = result.next



'''
Time Complexity:O(n)
Space Complexity:O(n)

'''