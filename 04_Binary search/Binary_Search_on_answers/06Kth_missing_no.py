# Brute Force Approach
class Solution:
    def Kth_missing(self,nums:list[int],k:int) ->int:
        temp1 = []
        temp2 = []
        for i in range(1,max(nums)):
            temp1.append(i)

        for i in temp1:
            if i not in nums:
                temp2.append(i) 
        return temp2[k-1] 

nums = [2,3,4,7,11]
object =Solution()
print(object.Kth_missing(nums,5))
'''
Time Complixity:O(n**2)
Space Complixity:O(n)

'''
# better Approach
class Solution:
    def kth_miss(self,nums:list[int],k:int) ->int:
        for i in range(len(nums)):
            if(nums[i]<=k):
                k+=1

            else:
                break
        return k
nums = [2,3,4,7,11]
object =Solution()  
print(object.kth_miss(nums,5))
'''
Time Complixity:O(n)
Space Complixity:O(1)   
'''

# optimized Approach
              

class Soution:
    def kth_miss(self,nums:list[int],k:int) ->int:
        start = 0
        end = len(nums)-1   
        while start<=end:
            mid = start + (end-start)//2
            miss = nums[mid] - (mid+1)
            if miss<k:
                start = mid+1
            else:
                end = mid-1
        return k + end + 1
nums = [2,3,4,7,11]
object =Soution()       
print(object.kth_miss(nums,5))
'''
Time Complixity::O(logn)
space Complixity:O(1)

'''    