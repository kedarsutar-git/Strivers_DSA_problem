
# Brute Force method
class Solution:
    def union(self,nums1:list[int],nums2:list[int]) -> list[int]:
        s = set()
        for i in range(len(nums1)):
            s.add(nums1[i])

        for i in range(len(nums2)):
            s.add(nums2[i])

            l = list(set(s))

        return l

nums1 = [1,2,3,4,5,6,7]            
nums2 = [1,8,9,10,11,23,98]
object = Solution()
print(object.union(nums1,nums2))     
'''
Time Complxity:O(n)
Space Complixity:O(n)
'''       


