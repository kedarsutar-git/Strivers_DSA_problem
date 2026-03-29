'''
nums = [-1,0,1,2,-1,-4]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

'''
# Brute force method:
def sum3(nums):
    s = set()
    temp =[]
    ans = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if(nums[i]+nums[j]+nums[k]==0):
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    s.add(tuple(temp))
    for n in s:
        ans.append(list(n))                            
            
    return ans
nums = [-1,0,1,2,-1,-4] 
print(sum3(nums))               

'''
Time Complixity:O(n**3)*log(triplets)
space Complixity :O(unique triplets)
'''

def sum3(nums):
    s1 = set()
    for i in range(len(nums)):
        target = -nums[i]
        s = set()
        for j in range(i+1,len(nums)):
                third = target - nums[j]
            
                if(third in s):
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    s1.add(tuple(temp))
                s.add(nums[j])
    
    ans = [list(temp) for temp in s1]
    return ans            
nums = [-1,0,1,2,-1,-4] 
print(sum3(nums))      

'''
Time complixity;O(n**2)
space complixty:O(n)
'''

# Optimal method:
class Solution:
    def Sum_3(self,nums:list[int]) -> list[list[int]]:
        temp = []
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            j = i+1
            k = len(nums)-1
            while(j<k):
                Sum = nums[i] + nums[j] + nums[k]
                if(Sum<0):
                    j+=1

                elif(Sum>0):
                    k-=1

                else:
                    temp.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1

                    while(j<k and nums[j]==nums[j-1]):
                        j+=1

        return temp
nums =  [-1,0,1,2,-1,-4] 
object = Solution()
print(object.Sum_3(nums))   

'''
Time Complixity:O(nlog(n) + n**2)
space Complixity :O(n)
'''







 