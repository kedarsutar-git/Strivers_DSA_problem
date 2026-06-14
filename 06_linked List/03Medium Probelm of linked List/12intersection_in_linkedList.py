'''
Ex :1
A = 1 -> 9 -> 1 -> 2 -> 4
B = 3 -> 2 -> 4

A: 1 -> 9 -> 1
                 \
                  2 -> 4
                 /
B:            3

output:2


EX:2
A = 4 -> 1 -> 8 -> 4 -> 5
B = 5 -> 6 -> 1 -> 8 -> 4 -> 5

A:    4 -> 1
             \
              8 -> 4 -> 5
              /
B: 5 -> 6 -> 1

output:8
'''
class Solution:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def intersection(self,headA,headB):
        d1,d2 = headA,headB

        while(d1!=d2):
            if(d1 is None):
                d1 = headB

            else:
                d1 = d1.next


            if(d2 is None):
                d2 = headA

            else:
                d2 =d2.next

        return d1
                                