class Solution:
    def PrintArr(self,arr:list[int],i:int):
        if(i==len(arr)):
            return
        
        print(arr[i],end=" ")
        self.PrintArr(arr,i+1)

object = Solution()
arr = [1,2,3,4,5,6,7,8,9]
object.PrintArr(arr,1)  



     