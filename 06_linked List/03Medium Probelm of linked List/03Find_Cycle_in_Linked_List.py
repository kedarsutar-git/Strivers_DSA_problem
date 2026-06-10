# Brute Force method
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def InCycle(self,head):
        Map = {}
        temp = head

        while(temp is not None):
            if(temp in Map):
                return True
            
            Map[temp]=1

            temp = temp.next

        return False

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''        

# optimal method

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def IsCycle(Self,head):
        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if(fast==slow):
                return True
        return False

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''
               