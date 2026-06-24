class Solution:
    def Maxnumber(self,arr:list[int],index:int,Max):
        if(index ==len(arr)):
            return Max
        
     
        if(arr[index]>Max):
            Max = arr[index]

        return self.Maxnumber(arr,index+1,Max)

object = Solution()
arr = [12,34,56,76]
print(object.Maxnumber(arr,0,arr[0]))
