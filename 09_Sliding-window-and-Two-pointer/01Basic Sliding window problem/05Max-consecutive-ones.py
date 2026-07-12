'''
Input : nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0] , k = 3
Output : 10

Explanation : The maximum number of consecutive 1's are obtained only if we flip the 0's present at position 3, 4, 5 (0 base indexing).
The array after flipping becomes [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0].
The number of consecutive 1's is 10.



Input : nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] , k = 3
Output : 9

Explanation : The underlines 1's are obtained by flipping 0's in the new array.
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1].
The number of consecutive 1's is 9.
'''

# Brute force method 
class Solution:
    def MaxConsecutiveOnes(self,nums:list[int],k:int) ->int:
        max_len = 0
        for i in range(len(nums)):
            zeros = 0
            for j in range(i,len(nums)):
                if(nums[j]==0):
                    zeros += 1

                if(zeros<=k):
                    length = j-i+1 
                    max_len= max(max_len,length)

                else:
                    break

        return max_len
object = Solution()
nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
print(object.MaxConsecutiveOnes(nums,3))           

'''
Time Complexity:O(n**2)
space Complexity:O(1)
'''

class Solution:
    def MaxConsecutiveOnes(self,nums:list[int],k:int) ->int:
        left , right = 0 ,0 
        Zeros = 0
        max_len = 0

        while(right<len(nums)):
            if(nums[right]==0):
                Zeros += 1

            while(Zeros>k):
                if(nums[left]==0):
                    Zeros -=1
                left += 1

            if(Zeros<=k):
                length = right - left + 1
                max_len = max(max_len,length)

            right +=1

        return max_len

object = Solution()
nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]

print(object.MaxConsecutiveOnes(nums,3))                        

'''
Time Complexity:O(n)
Space Complexity:O(1)

'''