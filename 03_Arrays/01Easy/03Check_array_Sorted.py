def sortarr(arr):
    n = len(arr)
    for i in range(1,n):
        if(arr[i] < arr[i-1]):
            return False
    return True

arr = [12,1,34]
print(sortarr(arr))


# leet code style 
class solution:
    def Check(self,nums:list[int]) -> bool:
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                return False
        
        return True    
               
        
nums = [12,13,14,15,16,17,18,19,2] 
object = solution()
print(object.Check(nums))

