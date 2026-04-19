# Brute force method
def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr

arr = [1,0,2,1,2,0]  
print(sort(arr))        

'''
Time complexity:O(n**2)
space complexity :O(1)

'''
# better method 
def Sort(arr):
    n = len(arr)
    count0 = 0
    count1 = 0
    count2 = 0
    for i in range(n):
        if(arr[i]==0):
            count0 += 1

        elif(arr[i]==1):
            count1 += 1

        else:
            count2 += 1        
        
    for i in range(count0):
        arr[i] = 0

    for i in range(count0,count0+count1):
        arr[i] = 1  

    for i in range(count0+count1,n):
        arr[i] = 2  

    return arr      
arr = [1,0,2,0,1,2,0,1,0]     
print(Sort(arr)) 
'''
Time complexity:O(2n)
Space complexity:O(1)
'''  


# optimal method 


class Solution:
    def Sort012(self,nums:list[int]) -> list[int]:
        start = 0
        mid = 0 
        end = len(nums)-1
        while(mid<=end):
            if(nums[mid]==0):
                nums[mid],nums[start] = nums[start],nums[mid]

                mid +=1
                start +=1

            elif(nums[mid]==1):
                mid+=1

            elif(nums[mid]==2):
                nums[mid],nums[end] = nums[end],nums[mid]
                end-=1

        return nums
nums = [1,1,1,1,0,1,2,2,2,2,2,0,1,2,0,2,2,2,0,1,0]
object = Solution()
print(object.Sort012(nums))   

'''
Time Complexity : O(n)
Space Complexity : O(1)
'''

                 

