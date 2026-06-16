# brute force method 
class Solution:
    def shipWithinDays(self, weights, days):
       for capacity in range(max(weights),sum(weights)+1):
        load  = 0
        day   = 1
        for weight in weights:
            if(load+weight>capacity):
                day += 1
                load = weight


            else:
                load+=weight

        if(day<=days):
            return capacity   
        
weights =   [3, 2, 2, 4, 1, 4]
object =Solution()
print(object.shipWithinDays(weights,3))       
        
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
        while(start <= end):
            mid = start +(end-start)//2

            days_needed = 1
            current_load = 0
            for weight in nums:
                if(current_load + weight > mid):
                    days_needed += 1
                    current_load = weight
                else:
                    current_load += weight
            if(days_needed <= days):
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


