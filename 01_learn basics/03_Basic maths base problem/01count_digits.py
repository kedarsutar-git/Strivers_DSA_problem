class Solution:
    def count(self,n:str) -> int:
        count = 0
        for i in  range(len(n)):
            count +=1

        return count
n = "1234567890"
object = Solution()
print(object.count(n))

'''
Time Complexity:O(n)
Sapce complexity:O(1)

'''            


