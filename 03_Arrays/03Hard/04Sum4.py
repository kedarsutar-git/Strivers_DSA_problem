# Brute force method
class Solution:
    def Sum4(self,nums:list[int],temp = [],s = set(),ans = []) ->list[list[int]]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for m in range(k+1,len(nums)):
                        if(nums[i]+nums[j]+nums[k]+nums[m]==0):
                            temp = [nums[i],nums[j],nums[k],nums[m]]
                            temp.sort()
                            s.add(tuple(temp))

        for n in s:
            ans.append(list(n))
        return ans 

nums = [1,0,-1,0,-2,2]
object =Solution()
print(object.Sum4(nums))             

'''
Time Complixity :O(n**4) 
space Complixity :O(n**4)
'''

# Optimal method
class Solution:
    def Sum_4(self,nums:list[int],tar:int,temp=[]) ->list[list[int]]:
        nums.sort()
        for i in range(len(nums)):
            if(i>0 and nums[i]==nums[i-1]):  
                continue
            for j in range(i+1,len(nums)):
                p = j+1
                q = len(nums)-1
                while(p<q):
                    sum = nums[i]+nums[j]+nums[p]+nums[q]                   
                    if(sum<tar):
                        p+=1

                    elif(sum>tar):
                        q-=1

                    else: # sum==0
                        temp.append([nums[i],nums[j],nums[p],nums[q]])
                        p+=1
                        q-=1
                        while(p<q and nums[p]==nums[p-1]):
                            p+=1
                j+=1        
                while(j<len(nums) and nums[j]==nums[j-1]):
                    j+=1
        return temp

nums = [1,0,-1,0,-2,2]
object = Solution()
print(object.Sum_4(nums,0))

'''
Time complixity :O(nlog(n) + n**3)
Space Complixity :O(Unique group to store in temp)
'''
