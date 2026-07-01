class Solution:
    def median(Self,nums1,nums2):
        i,j = 0,0
        temp = []
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                temp.append(nums1[i])
                i+=1

            else:
                temp.append(nums2[j])
                j+=1

        while(i<len(nums1)):
                temp.append(nums1[i])
                i+=1


        while(j<len(nums2)):
             temp.append(nums2[j])
             j+=1

        n = len(temp)
        if(n%2==1):
             return temp[n//2]
        
        return (temp[n//2-1]+temp[n//2])/2
    

nums1  = [2, 4, 6]
nums2 = [1, 3,5]

object =Solution()
print(object.median(nums1,nums2))    

'''
Time Complexity:O(n)
Space Complexity:O(n)

'''


