class Solution:
    def integerToBinary(self,num:int):
        binary_num = bin(num)

        return binary_num

num = 12
object = Solution()
print(object.integerToBinary(num))


