'''
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
'''

# Brute Force method 
class Node:
    def __init__(self,data,val = 0):
        self.data = data 
        self.next  = None 

class Solution:
    def MergeSortedList(self,list1,list2):
        arr = []
        temp1 = list1
        while(temp1 is not None):
            arr.append(temp1.val)

            temp1 = temp1.next


        temp2 = list2
        while(temp2 is not None):
            arr.append(temp2.val)

            temp2 = temp2.next 


        arr.sort()

        dummy = Node(-1)
        temp = dummy
        for num in arr:
            temp.next = Node(num)

            temp = temp.next

        return dummy.next    

'''
Time Complexity:O(n+m)+log(n+m)
Space Complexity:O(n+m)

'''


# Optimal method 
class Node:
    def __init__(self,data,val):
        self.data = data
        self.next = None

class Solution:
    def Merge(self,list1,list2):
        dummy = Node(-1)

        temp = dummy

        temp1 = list1
        temp2 = list2
        while(temp1 is not None and temp2 is not None):
            if(temp1.val>temp2.val):
                temp.next = temp1
                temp1 = temp1.next

            else:
                temp.next = temp2
                temp2 = temp2.next


            temp = temp.next

        if(temp1 is not None):
            temp.next =temp1

        else:
            temp.next = temp2


        return dummy.next

'''
TIme Complexity:O(n)
Space Complexity:O(1)
'''
                                