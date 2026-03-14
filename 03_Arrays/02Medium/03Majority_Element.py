# Brute Force method
# Using Two pointer Method
def Maj(arr):
    n = len(arr)
    frq = 0
    for i in range(n):
        for j in range(i,n):
            if(arr[i]==arr[j]):
                frq += 1

        if(frq>n/2):
            return arr[i]

arr = [1,2,1,2,1,2,2,2]
print(Maj(arr))                

'''
Time Complixity : O(n**2)
Space Complixity: O(1)
'''


# Better Method
# 1st sort 
def Majority(arr):
    n = len(arr)
    arr.sort()
    frq = 1
    ans = arr[0]
    for i in range(1,n):
        if(arr[i]==arr[i-1]):
            frq +=1

        else:
            frq = 1
            ans = arr[i]
        if(frq>n/2):
          return ans            
    return ans
arr = [0,1,2,0,1,2,2,1,2,2]

print(Majority(arr))
    
'''
Time Complixity : O(nlog(n))
Space Complixity : O(1)
'''  

# optimal method (Moores Voting Algorithm)
def Moores(arr):
    n = len(arr)
    frq = 0 
    ans = 0
    for i in range(n):
        if(frq ==0):
            ans= arr[i]

        if(ans== arr[i]):
            frq +=1 

        else:
            frq -=1

    return frq
arr = [0,1,2,0,1,2,2,1,2,2] 
print(Moores(arr))              