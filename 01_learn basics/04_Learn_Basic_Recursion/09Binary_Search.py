class Solution:
    def Bs(self,nums,start,end,tar):
    
        if(start<=end):
            
            mid = start+(end-start)//2
            if(nums[mid]==tar):
                return mid
        
            elif(nums[mid]<tar):
                return self.Bs(nums,mid+1,end,tar)

            else:
                return self.Bs(nums,start,mid-1,tar)
        return -1
    
nums = [1,2,3,4,5,6,7]
object =Solution()
print(object.Bs(nums,0,len(nums)-1,7))    

    
class Solution:
    def printNum(self,n:int):
        if(n==0):
            return
        self.printNum(n-1)
        print(n)

        

object =Solution()
print(object.printNum(5))

