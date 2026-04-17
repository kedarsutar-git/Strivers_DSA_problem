class Solution:
    def LargestOddNo(self,s:str) -> str:
        index = -1
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2==1):
                index = i
                break
        i = 0
        while(i<=index  and s[i]=="0"):
            i+=1

        return s[i:index+1]    

s = "003047987887"
object = Solution()
print(object.LargestOddNo(s))               
