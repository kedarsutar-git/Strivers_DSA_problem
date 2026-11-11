'''

'''
# Brute force method

class Solution:
    def minJump(self,nums,index,jump):
        if(index>=len(nums)-1):
            return jump
        minjump = float("inf")
                
        for i in range(1,nums[index]+1):
            minjump = min(self.minJump(nums,index+i,jump+1),minjump)

        return minjump

nums = [2,3,1,1,4]
object = Solution()
print(object.minJump(nums,0,0))


'''
Time Complexity:O(n**n)
Spcace Comlexity:O(1)

'''


# Optimal method (Greedy method)
class Solution:
    def MinJump(self,nums:list[int]) ->int:
        jump,far,near = 0, 0, 0
        while(far<len(nums)-1):
            farhest = 0

            for i in range(near,far+1):
                farhest = max(farhest,i+nums[i])

            near = far + 1
            far = farhest
            jump += 1

        return jump

nums = [2,3,1,1,4]
object = Solution()
print(object.MinJump(nums))

'''
Time Complexity:O(n)
Space Compelxity:O(1)

'''