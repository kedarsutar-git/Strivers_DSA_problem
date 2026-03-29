def LeftRotate(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(n-1):
        arr[i] = arr[i+1]


    arr[n-1] = temp
    return arr
arr = [1,2,3,4,5]
print(LeftRotate(arr))


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