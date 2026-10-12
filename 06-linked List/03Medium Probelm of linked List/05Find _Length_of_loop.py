'''
Example 1

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
Output: 4
Explanation: 2 -> 3 -> 4 -> 5 - >2, length of loop = 4.



Example 2

Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
Output: 0
Explanation: No loop is present in the linked list.
'''

class Solution:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def FindLoop(self,head):
        temp = head 
        Map = {}
        timer = 1

        while(temp is not None):
            if(temp in Map):
                val = Map[temp]

                return timer-val
            Map[temp] = timer
            timer +=1
            temp = temp.next

        return 0

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
    def FondLength(Self,head):
        slow = head
        fast = head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

            if(fast==slow):
                count = 1

                fast = fast.next

                while(fast!=slow):
                    fast = fast.next
                    count+=1

                return count

        return 0

'''
Time Complexity:O(n)
Sapce Complexity:O(1)
'''
        

