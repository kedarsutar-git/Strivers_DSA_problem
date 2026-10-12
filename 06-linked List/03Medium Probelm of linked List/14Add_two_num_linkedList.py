'''
Example 1

Input: linkedList1 = [5, 4], linkedList2 = [4]
Output: [9, 4]

Explanation: linkedList1 = 45, linkedList2 = 4.
linkedList1 + linkedList2 = 45 + 4 = 49.
The sum is 49 and when prepare the linked list we reverse the number [9, 4]



Example 2

Input: linkedList1 = [4, 5, 6], linkedList2 = [1, 2, 3]
Output: [5, 7, 9]

Explanation: linkedList1 = 654, linkedList2 = 321.
linkedList1 + linkedList2 = 654 + 321 = 975.
The sum is 975 and when prepare the linked list we reverse the number [5, 7, 9]The sum
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry

            if l1:
                total += l1.data
                l1 = l1.next

            if l2:
                total += l2.data
                l2 = l2.next

            carry = total // 10

            temp.next = ListNode(total % 10)
            temp = temp.next

        return dummy.next15