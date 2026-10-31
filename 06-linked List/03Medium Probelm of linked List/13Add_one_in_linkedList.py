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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def addOne(self,head):
        ans = []
        temp = head
        while(temp is not None):
            ans.append(temp.data)
            temp = temp.next

        for i in range(len(ans)-1,-1,-1):
            if ans[i]!=9:
                ans[i] += 1

                break
            else:       # ans[i]==9
                ans[i] = 0

            ans = [1] + ans
        

        k = 0 
        temp = head
        while(temp is not None):
            temp.data = ans[k]
            temp = temp.next

            k += 1

        return head




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

object = Solution()
result = object.addOne(head)
print(result)
while(result is not None):
    print(result.data,end= "->")

    result = result.next

print(None)

arr1 = [123]
arr2 = [1]
print(arr1+arr2)