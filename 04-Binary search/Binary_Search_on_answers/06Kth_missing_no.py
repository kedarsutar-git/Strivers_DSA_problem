# Brute Force Approach
class Solution:
    def KthmissingNo(self,nums:list[int],k:int) ->int:
        l1 = []
        l2 = []
        for i in range(1,max(nums)+k+1):    # We add k because the kth missing number may be greater than max(nums).
            l1.append(i)
        for num in l1:
            if(num not in nums):
                l2.append(num)

        return l2[k-1]

object =Solution()
nums =[2,3,4,7,11]
print(object.KthmissingNo(nums,5))

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







