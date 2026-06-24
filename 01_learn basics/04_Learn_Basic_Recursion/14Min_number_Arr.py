class Solution:
    def MinNumber(self,arr:list[int],index:int,Min):
        if(index==len(arr)):
            return Min
        
        if(arr[index]<Min):
            Min = arr[index]

        return self.MinNumber(arr,index+1,Min)

arr = [12,34,456,567,34,6,7,1234]
object = Solution()
print(object.MinNumber(arr,0,arr[0]))        