
'''
Summary of Insertion Sort:

1.Insertion Sort takes one element at a time and places it in its correct position in the sorted part of the array.
2.It starts from the second element because the first element is already considered sorted.
3.Larger elements are shifted to the right to make space for the current element.
4.This process repeats until all elements are arranged in sorted order.
'''
class Solution:
    def insertion_sort(self,arr:list[int]) ->list[int]:

        for i in range(1, len(arr)):
            key = arr[i]    # element to be inserted
            j = i - 1

            # move elements greater than key one position ahead
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1

            # insert key at correct position
            arr[j + 1] = key

        return arr

arr = [12,34,56,21,43,54] 
object = Solution()

print(object.insertion_sort(arr))   

'''
Time Complexity:O(n)
Space Complexity:O(1)

''' 
 




