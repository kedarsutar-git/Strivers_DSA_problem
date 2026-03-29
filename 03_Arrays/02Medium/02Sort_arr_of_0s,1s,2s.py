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
Time complixity:O(n**2)
space complixity :O(1)

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
Time complixity:O(2n)
Space complixity:O(1)
'''  


# optimal method 

def Sort012(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n-1
    while(mid<=high):
        if(arr[mid]==0):
            temp = arr[low]
            arr[low] = arr[mid]
            arr[mid] = temp

            low +=1
            mid +=1

        elif(arr[mid]==1):
            mid +=1

        elif(arr[mid]==2):
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp

            high -=1
    return arr


arr = [2,0,2,1,1,0,1,2,0,0]
print(Sort012(arr)) 

'''
Time Complixity : O(n)
Space Complixity : O(1)
'''

# leet code style 
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

