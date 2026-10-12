'''
You are given an integer n.

Print all the prime numbers till n (including n).

A prime number is a number that has only two divisor's 1 and the number itself.

Example 1:
Input : n = 7

Output : [2, 3, 5, 7]

Explanation : The number 2 has only two divisors 1 and 2.

The number 3 has only two divisors 1 and 3.

The number 5 has only two divisors 1 and 5.

The number 7 has only two divisors 1 and 7.

Example 2:
Input : n = 2

Output : [2]

Explanation : There is only one number 2 that is a prime till 2.
'''

class Solution:
    def primenums(self,n:int) ->list[int]:
        temp = []
        for i in range(2,n+1):
            count = 0
            for j in range(1,i+1):
                if(i%j==0):
                    count+=1

            if(count==2):
                temp.append(i)
        return temp

n = 7
object =Solution()
print(object.primenums(n))
