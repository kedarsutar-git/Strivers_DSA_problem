'''
EX:1
Input: 1->2->3->4->5 
Output: 1->2->4->5

Explanation: Node with value 3 is at the middle node and deleted.



EX:2
Input: 1->2->3->4
Output: 1->2->4

Explanation: The linked list has an even number of nodes hence we
delete the second middle node which is 3.

'''
# Brute Force Method 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def DeleteMid(self,head):
        if(head is None or head.next is None):
            return None 
        temp =head 
        count = 0
        while(temp is not None):
            count +=1

            temp = temp.next

        mid = count//2

        temp = head 
        while(temp is not None):
            mid -=1

            if(mid==0):
                temp.next = temp.next.next
                break
            temp =temp.next

        return head    

'''
Time Complexity:O(2n):
Space Complexity:O(1)
'''

# Optimal method 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def DeleteMiddle(Self,head):
        if(head is None or head.next is None):
            return None
        
        slow = head
        fast = head.next.next

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next    
            
        return head 
    
'''
Time Complexity:O(n)
Space complexity:O(1)

'''    
    




        