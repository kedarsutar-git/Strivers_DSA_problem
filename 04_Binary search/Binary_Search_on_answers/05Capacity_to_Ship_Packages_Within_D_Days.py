# brute force method 
class Solution:
    def shipWithinDays(self, nums, days):
       for capacity in range(max(nums),sum(nums)+1):
        Sum,day = 0,1
        for num in nums:
           
            if(Sum+num<=capacity):
                Sum+=num

            else:
                day+=1
                Sum = num    

        if(day<=days):
            return capacity
        
nums =   [3, 2, 2, 4, 1, 4]
object =Solution()
print(object.shipWithinDays(nums,3))       
        
'''
| Method        | Time Complexity                   | Space Complexity |
| ------------- | --------------------------------- | ---------------- |
| Brute Force   | (O((S-M+1)\cdot n)) or (O(Sn))    | (O(1))           |


'''       


# Optimal Mehtod

class Solution:
    def Least_capacity(self,nums:list[int],days:int) -> int:
        start = max(nums)
        end = sum(nums)
        while start <= end:
            mid = (start + end) // 2
            days_needed = 1
            current_load = 0
            for weight in nums:
                if current_load + weight > mid:
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
            if days_needed <= days:
                end = mid - 1
            else:
                start = mid + 1
        return start    
nums = [1,2,3,4,5,6,7,8,9,10]
  
object = Solution()

print(object.Least_capacity(nums,5))

'''
| Method        | Time Complexity                   | Space Complexity |
| ------------- | --------------------------------- | ---------------- |
| Binary Search | (O(n\log(S-M+1))) or (O(n\log S)) | (O(1))           |

'''
