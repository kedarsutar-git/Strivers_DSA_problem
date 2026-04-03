'''
Floor : largest number in the array <= x

ceil : Smallest number in the array >= x

working and condition of ceil and lower bound is same 


Ex.1:
arr = [10,20,30,40,50]
x = 25

Floor : 20(largest no in the array and less or equal to 25)
ceil  : 30(Smallest no in the array and greter or equal to 25)


Ex.2:
arr = [3, 4, 4, 7, 8, 10]
x= 5
Floor : 4
ceil : 7


Ex.3:
arr =[3, 4, 4, 7, 8, 10]
x= 8

Floor : 8
ceil : 8

'''

class Solution:
    def Floor_Ceil(self,nums:list[int],x:int) -> int:
        for i in range(len(nums)):
            if(nums[i] > x):
                return nums[i-1],nums[i]  
            
            elif(nums[i]==x):
                return nums[i],nums[i]
            

nums  = [10,20,30,40,50]
object = Solution()
print(object.Floor_Ceil(nums,25))    

'''
Time Complixity:O(n)
space Complixity :O(1)
'''

