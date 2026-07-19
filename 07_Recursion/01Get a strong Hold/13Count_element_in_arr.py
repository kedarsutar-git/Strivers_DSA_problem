class Solution:
    def CountNum(self,arr:list[int],index:int,target:int,count:int):
        if(index>=len(arr)):
            print(count)
            return 
        if(arr[index]==target):
            count+=1
        
        return self.CountNum(arr,index+1,target,count)
    
arr = [12,12,34,56,78,12,12,56,76,6512]
object = Solution()
print(object.CountNum(arr,0,12,0))    
    


