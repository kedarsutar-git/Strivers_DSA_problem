def intersection(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    temp = []

    for i in range(n1):
        for j in range(n2):
            if(arr1[i]==arr2[j]):
                if(arr1[i] not in temp):
                    temp.append(arr1[i])
                
    return temp

arr1 = [1,2,3,4,5]
arr2 = [1,3,5,6,8]

print(intersection(arr1,arr2))


# leet code style 
class Solution:
    def intersection(self,num1:list[int],num2:list[int]) -> list[int]:
        temp = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                if(num1[i] ==num2[j]):
                    temp.append(num1[i])

        return temp

num1 = [1,2,3,4,5]
num2 = [1,3,5,6,8]    
object = Solution()
print(object.intersection(num1,num2))          