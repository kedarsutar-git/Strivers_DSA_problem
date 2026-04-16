def check(arr):
    n = len(arr)
    if(n==0):
        return 0
    i = 0
    for j in range(1,n):
        if(arr[i]!=arr[j]):
           i = i+1    
           arr[i]=arr[j]


    return i+1
arr = [1,1,2,2,3,3,3,4] 
print(arr[:check(arr)])   

# leetcode style
class Solution:
    def Removedup(self,nums:list[int]) ->list[int]:
        s = set()
        for n in nums:
            s.add(n)
            l = list(set(s))

        return l

nums = [1,2,3,4,4,5,6]
object = Solution()
print(object.Removedup(nums))   

'''
Time ComplixityO(n)
Space Complxity(n)
'''