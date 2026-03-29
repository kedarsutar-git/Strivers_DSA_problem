# brute force method
def Subarray(arr):
    n = len(arr)
    tar = 5
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
           sum += arr[j]
           if(sum==tar):
              count = count+1
        
    return count                                                             
arr = [1,2,3,4,6,7,8]
print(Subarray(arr))

'''
Time complixity:O(n**2)
space complixity:O(1)
'''

# optimal method(prefix sum method):
    
def subarr(arr):
    k = 33
    count = 0
    D = {}
    ps = [0] * len(arr)

    ps[0] = arr[0]              
    for i in range(1, len(arr)):       
        ps[i] = ps[i-1] + arr[i]

    for j in range(len(arr)):          
        if ps[j] == k:
            count += 1
        val = ps[j] - k
        if val in D:
            count += D[val]
        D[ps[j]] = D.get(ps[j], 0) + 1   

    return count

arr = [9, 4, 20, 3, 10, 5]
print(subarr(arr)) 




class Solution:
    def SubArr(self,nums:list[int],tar:int) -> int:
        count = 0 
        for i in range(len(nums)):
            sum = 0 
            for j in range(i,len(nums)):
                sum += nums[j]

                if(sum==tar):
                    count +=1

        return count

nums = [9, 4, 20, 3, 10, 5]         
object = Solution()
print(object.SubArr(nums,33))       