class Solution:
    def RemoveMiddle(self,Stack:list[int]) ->None:
        n = len(Stack)
        count = 0
        for i in range(n):
            count +=1
            if(count==n//2):
                Stack.pop(i)
                break
        return Stack
Stack = [1,2,3,4,5]
object = Solution()
print(object.RemoveMiddle(Stack))

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''