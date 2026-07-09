
'''
Example 1:
Input:
nums = [1, 2, 1, 3, 5, 2]
Output:
 [3, 5]
Explanation:
The integers 3 and 5 have appeared only once.



Example 2:
Input:
 nums = [-1, 0]
Output:
 [-1, 0]
Explanation:

The integers -1 and 0 have appeared only once.
'''

class Solution:
    def Primefac(self,nums:list[int]) ->list[int]:
        Map = {}
        for num in nums:
            if num in Map:
                Map[num] += 1

            else:
                Map[num] = 1

        
        temp = []

        for key ,value in Map.items():
            if(self.isodd(value)):
                temp.append(key) 

        return temp

    def isodd(self,value):
            if(value%2==0):
                return False  

            return True 

nums = [-1, 0]
object = Solution()
print(object.Primefac(nums))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''