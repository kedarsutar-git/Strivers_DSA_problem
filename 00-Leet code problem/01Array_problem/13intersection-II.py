'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times
as it shows in both arrays and you may return the result in any order.

 

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
class Solution:
    def Intersection(self,nums1:list[int],nums2:list[int]) ->list[int]:
        temp = []

        arr1 = sorted(nums1)
        arr2 = sorted(nums2)
        i,j=0,0

        while(i<len(arr1) and j<len(arr2)):
            if(arr1[i]<arr2[j]):
                i+=1

            elif(arr1[i]>arr2[j]):
                j+=1

            else:
                temp.append(arr1[i])

                i+=1
                j+=1

        return temp

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

object = Solution()
print(object.Intersection(nums1,nums2))

'''
Time Complexity:O(n)
Space Complexity:O(n)
'''





         
