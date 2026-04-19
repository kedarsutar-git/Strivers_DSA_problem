# Brute Force method
# Using Two pointer Method
def Maj(arr):
    n = len(arr)
    frq = 0
    for i in range(n):
        for j in range(i,n):
            if(arr[i]==arr[j]):
                frq += 1

        if(frq>n/2):
            return arr[i]

arr = [1,2,1,2,1,2,2,2]
print(Maj(arr))                

'''
Time Complexity : O(n**2)
Space Complexity: O(1)
'''


# Better Method
# 1st sort 
def Majority(arr):
    n = len(arr)
    arr.sort()
    frq = 1
    ans = arr[0]
    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            frq +=1

        else:
            frq = 1
            ans = arr[i]
        if(frq>n/2):
          return ans            
    return ans
arr = [0,1,2,0,1,2,2,1,2,2]

print(Majority(arr))
    
'''
Time Complexity : O(nlog(n))
Space Complexity : O(1)
'''  

# optimal method (Moores Voting Algorithm)
class Solution:
    def majority(self,nums:list[int]) -> int:
        frq = 0
        ans = 0
        for i in range(len(nums)):
            if(frq ==0):
                ans = nums[i]

            if(ans==nums[i]):
                frq+=1

            else:
                frq-=1

        return ans 
nums = [1,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4]
object = Solution()
print(object.majority(nums))         
'''
Time Complexity : O(n)
Space Complexity :O(1)

Note : majority element > n/2     n=len(arr)
'''


                    