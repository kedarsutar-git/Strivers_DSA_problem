'''
EX:1
Input: 4->5->6
Output: 4->5->7

Explanation: 456 + 1 = 457

EX:2
Input: 9->9->9
Output: 1->0->0->0

Explanation: 999 + 1 = 1000
'''

class Node:
    def __init__(self,data,val=0):
        self.data = data
        self.next = None

class Solution:
    def Addone(self,head):
        arr = []
        temp = head 

        while(head is not None):
            arr.append(temp.val) 

            temp = temp.next

        for i in range(len(arr)-1,-1,-1):
            if(arr[i]!=9):
                arr[i]+=1
                break

            else:
                arr[i]=0

        else:
            arr = [1]+arr


        head = Node(arr[0])
        temp = head 
        for i in range(1,len(arr)):
            temp.next = Node(arr[i])

            temp = temp.next

        return head 

'''
Time Complexity:O(n)+O(n)+O(n) = O(n)
Space Complexity:O(n)

'''         