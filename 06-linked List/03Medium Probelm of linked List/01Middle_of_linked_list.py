'''
Input: head = [1,2,3,4,5]
Output: 3
Explanation: The middle node of the list is node 3.



Input: head = [1,2,3,4,5,6]
Output: 4
Explanation: Since the list has two middle nodes with 
values 3 and 4, we return the second one.
 
'''
# Brute force method 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def MiddleNode(self,head):
        if(head is None or head.next is None):
            return head

        current = head
        count = 0
        while(current is not None):
            count += 1
            current = current.next 

        mid = (count//2)+1

        current = head
        i = 1
        while(i<mid):
            current = current.next
            i+=1
        return current    

'''
Time Complexity:O(n+n/2) = O(n)
Space Complexity:O(1)

'''               



# optimal mehthod 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def MiddleNode(self,head):
        if(head is None or head.next is None):
            return head

        slow = head
        fast = head 
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow

'''
Time Complexity:O(n)
Sapce Complexity:O(1)

'''






