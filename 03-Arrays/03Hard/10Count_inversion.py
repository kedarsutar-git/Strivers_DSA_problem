# Brute Force method
'''
In the given array two Cases are satisfy :

Case.1: i<j (indexing of the element)

Case.2: nums[i] > nums[j] (Element in the array)
'''
class Solution:
    def CountInversion(self,nums:list[int]) ->int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(i<j and nums[i]> nums[j]):
                    count +=1 


        return count

nums = [1,3,5,10,2,6,8,9]
object = Solution()
print(object.CountInversion(nums))

'''
Time complixity :O(n**2)
Space Complixity :O(1)

'''


# optimal method :

def merge_Sort(arr,start,end):
    if(start<end):
        mid = start +(end - start)//2

        leftinvcount = merge_Sort(arr,start,mid)   # left array
        Rightinvcount  = merge_Sort(arr,mid+1,end)   # Right array

        invcount = merge(arr,start,mid,end)    # merge sort call

        return leftinvcount+Rightinvcount+invcount
    
    return 0  
def merge(arr,start,mid,end):
    temp =[]
    i = start
    j = mid+1
    invcount = 0
    while(i<=mid and j<=end):
        if(arr[i] <= arr[j]):
            temp.append(arr[i])
            i = i+1

        else:
            temp.append(arr[j])
            j = j+1
            invcount+= (mid -i +1)
    while(i<=mid):
        temp.append(arr[i])
        i = i + 1

    while(j<=end):
        temp.append(arr[j])
        j = j + 1


    return invcount    

arr = [1,3,5,10,2,6,8,9] 

count = merge_Sort(arr,0,len(arr)-1)

print(f"The inversion pair count of the given array is: {count}")


