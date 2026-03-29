class Solution:
    def PascalTriange(self,column:int,row:int) -> int:
        row  = min(row,column-row)
        res = 1
        for i in range(row):
            res = res*(column-i)
            res = res//(i+1)
        return res
object = Solution()
print(object.PascalTriange(5,2)) 

