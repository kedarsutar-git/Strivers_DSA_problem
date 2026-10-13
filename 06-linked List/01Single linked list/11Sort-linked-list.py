'''
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def SortLinkedList(self,head):
        Current = head
        arr = []

        while(Current is not None):
            arr.append(Current.data)
            Current = Current.next

        array = sorted(arr)

        k = 0
        Current = head
        while(Current is not None):
            Current.data = array[k]
            Current = Current.next
            k += 1

        return head

head = Node(1)
head.next = Node(9)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(3)

object = Solution()

result = object.SortLinkedList(head)

while(result):
    print(result.data, end="->")
    result = result.next


'''
Time Complexity:O(n)
Space Complexity:O(n)

'''