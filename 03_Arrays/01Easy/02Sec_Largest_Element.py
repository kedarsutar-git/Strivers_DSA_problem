# optimal solution
class Solution:
    def Secondlargest(self,nums:list[int]) ->int:
        largest = max(nums)
        secondlargest = -1
        for num in nums:
            if(num!=largest):
                secondlargest = max(num,secondlargest)

        return secondlargest
nums = [1,2,3,7,6,5,9]
object =Solution()
print(object.Secondlargest(nums))  

'''
Time Complexity:O(n)
space Complexity:O(1)
'''


# optimal method
        
class Solution:
    def SecondLargestElement(self,nums:list[int]) ->int:
        largest = 0
        second_largest = 0
        for num in nums:
            if(num>largest):
                second_largest = largest
                largest = num

            elif(num>second_largest and num !=largest):
                second_largest = num

        return second_largest

nums = [12,32,43,45,67,78]
object = Solution()
print(object.SecondLargestElement(nums))

'''
Time Complexity:O(n)
Sacpe Complexity:O(1)

'''



