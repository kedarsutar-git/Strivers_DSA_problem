'''
def BubbleSort(arr):
    n = len(arr)

    for i in range(n,0,-1):

        for j in range(i-1):
            if(arr[j]>arr[j+1]):


                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr 

arr = [12,34,11,7,45,15] 

print(BubbleSort(arr))
'''

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp

    return arr
arr = [12,332,1,34,21,43,56]
print(bubbleSort(arr))            
