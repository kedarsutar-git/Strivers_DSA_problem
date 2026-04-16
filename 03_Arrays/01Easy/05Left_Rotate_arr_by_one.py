# Brute Force method
class Soution:
    def L_Rotate(self,nums:list[int]) -> list[int]:
        temp = nums[0]
        for i in range((len(nums))-1):
            nums[i] = nums[i+1]

        nums[len(nums)-1] = temp

        return nums
nums = [10,11,12,13,14,15]
object = Soution()
print(object.L_Rotate(nums))   
'''
Time Complixity:O(n)
Space Complixity(n)
'''  