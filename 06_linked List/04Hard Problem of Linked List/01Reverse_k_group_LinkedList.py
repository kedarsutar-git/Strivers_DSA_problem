
'''
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        count = 0
        temp = head

        while count < k:
            if temp is None:
                return head
            temp = temp.next
            count += 1

        prevNode = self.reverseKGroup(temp, k)

        temp = head
        count = 0

        while count < k:
            nextNode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextNode
            count += 1

        return prevNode
    
'''
Time Complexity:O(n/k)
Space Complexity:O(1)

'''
