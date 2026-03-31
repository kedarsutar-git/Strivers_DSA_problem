'''
XOR operator:
5^3:
     
5  = 1 0 1
3  = 0 1 1
     1 1 0 =  6

5^3 = 6

Important properties in DSA:

1. A^0 = A
2. A^A = 0
3. A^B^A = A
4. A^B =B^A

'''
# brute force method
class Solution:
    def XOR_arr(self,nums:list[int]) -> int:
        count = 0
        k = 6
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]^nums[j]==k):
                    count +=1 

        return count
    
nums = [4,2,2,6,4]
object = Solution()
print(object.XOR_arr(nums))


'''
Time Complixity :O(n**2)
space Complixity :O(1)
'''


                

