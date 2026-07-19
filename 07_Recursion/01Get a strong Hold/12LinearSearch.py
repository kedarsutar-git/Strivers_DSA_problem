class Solution:
    def search(self,arr:list[int],index:int,target:int):

        if(index==len(arr)):   # Base Case
            return -1
        
        if(arr[index]==target): # work
            return index
        
        
        return self.search(arr,index+1,target)  # Call
    
arr = [12,23,45,67]
object= Solution()
print(object.search(arr,0,67))    




 
    
    
      
