
class Solution:
    def RotateMatrix(self,nums:list[list[int]]) ->list[list[int]]:
        temp = [[0]*len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                temp[j][len(nums)-1-i] = nums[i][j]

        return temp

nums = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]] 

object =Solution()
print(object.RotateMatrix(nums))

'''
Time Complexity :O(n**2)
Space Complexity :O(n**2)
'''        

# optimal method
# 1. transpose 
# 2. Reverse each row



class Solution:
    def RotateMatrix(self,nums:list[list[int]]) ->list[list[int]]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                nums[i][j],nums[j][i]=nums[j][i],nums[i][j]

        for row in range(len(nums)):
            i = 0
            j = len(nums)-1
            while(i<=j):
                nums[row][i],nums[row][j] = nums[row][j],nums[row][i]    
 
                i+=1
                j-=1

        return nums

nums = [[1, 2,  3, 4],
        [5, 6,  7, 8],
        [9,10, 11,12],
        [13,14,15,16]
        ] 

object =Solution()
print(object.RotateMatrix(nums))  
'''
Time complexity :O(n**2) + O(n)
space Complexity :O(1)
'''