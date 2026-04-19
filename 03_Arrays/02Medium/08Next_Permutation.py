# Optimal method
class Solution:
    def NextPermutation(self,nums:list[int]) -> list[int]:
        # Step 1 :Find Pivot in the array 
        Pivot = -1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i] < nums[i+1]):
                Pivot = i
                break
        # Step 2 :In the array there are not pivot then reverse the array
        if(Pivot == -1):
            i = 0
            j = len(nums)
            while(i<=j):
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j-=1
        # Step 3 :swap the pivot and number and find the number(Exact greater then the pivot)
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]>nums[Pivot]):
                nums[i],nums[Pivot] = nums[Pivot],nums[i]
                break
        
        # Step 4 :Reverse the array form (pivot+1 to Len(nums)-1)
        i = Pivot+1
        j = len(nums) - 1

        while(i<=j):
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1

        return nums

nums = [1,2,3,6,5,4]
object = Solution()
print(object.NextPermutation(nums)) 

'''
Time Complexity : O(n)
Space Complexity : O(1)

'''