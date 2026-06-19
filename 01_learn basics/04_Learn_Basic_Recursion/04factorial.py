class solution:
    def Factorial(self,num:int) ->int:
        if(num==0 or num==1):
            return 1
        else:
            return num*self.Factorial(num-1)
        
num = 5
object = solution()
print(object.Factorial(num))

'''
Time Complexity:O(n)
Space Complexity:O(1)
'''
