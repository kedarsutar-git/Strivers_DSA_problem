class solution:
    def Factorial(self,num:int) ->int:
        if(num==0 or num==1):    # base Case
            return 1
        else:
            return num*self.Factorial(num-1)  # work and function call
        
num = 5
object = solution()
print(object.Factorial(num))

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''
