# brute force method
def Subarray(arr):
    n = len(arr)
    tar = 5
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
           sum += arr[j]
           if(sum==tar):
              count = count+1
        
    return count                                                             
arr = [1,2,3,4,6,7,8]
print(Subarray(arr))

'''
Time complixity:O(n**2)
space complixity:O(1)
'''

# optimal method(prefix sum method):

def subarr(arr):
    n = len(arr)
    k = 33
    count = 0
    ps = []
    ps[0]==arr[0]
    for i in range(n):
        ps[i]=ps[i-1]+arr[i]

        count = 0
        D = {}
        for j in range(n):
            if(ps[j]==k):
                count +=1
            val = ps[j]-k
            
arr = [9,4,20,3,10,5]
print(subarr(arr))

