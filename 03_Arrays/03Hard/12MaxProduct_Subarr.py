# Use kadanes algorithm(for only positive array)
class Solution:
    def MaxProduct(self,nums:list[int]) -> int:
        current_product = nums[0]
        Max_product = nums[0]

        for i in range(1,len(nums)):
            current_product = max(nums[i],current_product*nums[i])

            Max_product = max(Max_product,current_product)

        return Max_product

nums = [2,3,-2,4]
object = Solution()
print(object.MaxProduct(nums))

'''
Time Complixity :O(n)
space Complixity :O(1)
'''


# Brute force method

class Solution:
    def MaxPor(self,nums:list[int]) ->int:
        Max_pro = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                product = 1

                for k in range(i,j+1):
                    product = product*nums[k]

                    Max_pro = max(Max_pro,product)

        return Max_pro
nums = [2,3,-2,4]
object = Solution()
print(object.MaxPor(nums))

'''
TIme Complixity :O(n**3)
Space Complixity :O(1)
'''

# Better method
class Solution:
    def MaxPor(self,nums:list[int]) ->int:
        Max_pro = 0
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                product = product*nums[j]
                Max_pro = max(Max_pro,product)

        return Max_pro
nums = [2,3,-2,4]
object = Solution()
print(object.MaxPor(nums))

'''
Time Complixity :O(n**2)
Space Complixity:O(1)
'''

# optimal method

class Solution:
    def MaximunPro(self,nums:list[int]) -> int:
        prifix = 1
        sufix = 1
        Max = 0
        for i in range(len(nums)-1):
            if(prifix==0):
                prifix = 1

            if(sufix==0):
                sufix = 1

            prifix = prifix*nums[i]

            sufix = sufix * nums[i]

            Max = max(Max,prifix,sufix)

        return Max 
nums = [2,3,-2,4]
object = Solution()
print(object.MaximunPro(nums)) 