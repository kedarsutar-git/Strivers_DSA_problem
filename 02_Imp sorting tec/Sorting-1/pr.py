class Soluntion:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if(arr[j]> arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp

        return arr
arr = [7,6,5,4,3,21]
object = Soluntion()
print(object.bubbleSort(arr))

