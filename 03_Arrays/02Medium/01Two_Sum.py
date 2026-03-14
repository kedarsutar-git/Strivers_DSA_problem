# Brute force method 
def TwoSum(arr):
    n = len(arr)
    tar = 30
    for i in range(n):
        for j in range(i+1,n):
            arr[i]+arr[j]
            if(arr[i]+arr[j]==tar):
                return 1

            else:
                return 0
arr = [1,2,3,4,5,6]
print(TwoSum(arr))    
   
'''
Time Complixity: O(n**2)
space Complixity:O(1)

'''   
# optimal method
def twoSum(arr):
    n = len(arr)
    tar = 10
    D = {}
    for i in range(n): # O(n)
        first = arr[i]
        sec = tar - first
        if sec in D:
            return [D[sec],i] # O(1)

        D[first] = i
arr = [1,2,3,4,5,6]
print(twoSum(arr))

