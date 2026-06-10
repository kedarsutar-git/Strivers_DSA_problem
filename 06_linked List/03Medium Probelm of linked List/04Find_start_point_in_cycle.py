# Brute Force method
class Node:
     def __init__(self, data):
         self.data = data
         self.next = None

class Solution:
    def detectCycle(self, head):
        Map  = {}
        temp = head
        while(temp is not None):
            if(temp in Map):
                return temp

            Map[temp] = 1

            temp = temp.next

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''

# Optimal 
class Solution:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def StartPoint(self,head):
        slow = head
        fast = head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if(fast==slow):
                slow = head
                while(slow!=fast):
                    slow = slow.next
                    fast = fast.next

                return slow

        return None

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''     

