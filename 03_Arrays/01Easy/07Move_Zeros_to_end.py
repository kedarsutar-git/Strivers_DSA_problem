def Zeros_to_end(arr):
    j = -1
    n = len(arr)
    for i in range(n):
        if(arr[i]==0):
            j = i 
            break
    if(j==-1):
        return arr    
    for i in range(j+1,n):
        if(arr[i]!=0):
            temp = arr[i]
            arr[i] = arr[j]

            arr[j] = temp
            j = j+1

    return arr

arr = [1,0,3,4,0,5,0,9]

print(Zeros_to_end(arr))


# leetcode style 

class Solution:
    def movezero(self,nums:list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[i],nums[j] = nums[j],nums[i]

                j+=1
nums = [1,2,3,4,0,0,20,4,3,0]
obj = Solution()
obj.movezero(nums)
print(nums)

      




