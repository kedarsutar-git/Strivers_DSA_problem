class Solution:
    def Prime(self,num:int) ->str:
        for i in range(2,num):
            if(num%i==0):
                print("The number is not prime")
                break
            else:
                print("The number is prime")

num = 123
object =Solution()
print(object.Prime(num))                

'''
Time Complexity:O(n)
Space Complexity
'''