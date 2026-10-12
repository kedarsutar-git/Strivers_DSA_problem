#  using Extra space 
class Solution:
    def MergeArr(self,nums1:list[int],nums2:list[int]) -> list[int]:
        temp = []

        for i in range(len(nums1)):
            temp.append(nums1[i])
        for i in range(len(nums2)):
            temp.append(nums2[i])

            temp.sort()

        return temp 
       

nums1 = [8,9,10,11,12]
nums2 = [1,2,4,6,7]                
object = Solution()
print(object.MergeArr(nums1,nums2))

'''
Time complixity :O(n+m)
space Complixity :O(n)

'''

# optimal method        
class Solution:
    def Mergearr(self, nums1, n, nums2, m):
        i = n - 1
        j = 0

        while i >= 0 and j < m:
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                i -= 1
                j += 1
            else:
                break 

        nums1[:n] = sorted(nums1[:n])
        nums2[:m] = sorted(nums2[:m])

        nums1[n:] = nums2[:m]

        return nums1   

nums1 = [1, 2, 4, 6, 7, 0, 0, 0, 0, 0]
n  = 5

nums2 = [8, 9, 10, 11, 12]
m = 5
obj = Solution()
print(obj.Mergearr(nums1, n, nums2, m))

'''
Time complixity :O(n,m) + O(nlogn) +O(mlogm)
Space Complixity :O(1)
'''






