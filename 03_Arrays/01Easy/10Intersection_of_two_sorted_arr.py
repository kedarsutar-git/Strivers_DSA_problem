class Solution:
    def intersection(self,num1:list[int],num2:list[int]) -> list[int]:
        temp = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                if(num1[i] ==num2[j]):
                    if(num1[i] not in temp):
                        temp.append(num1[i])

        return temp

num1 = [1,2,3,4,5]
num2 = [1,3,5,6,8]    
object = Solution()
print(object.intersection(num1,num2))    
'''
Time Complexity:(n**2)
Space Complexity:(n)
'''      