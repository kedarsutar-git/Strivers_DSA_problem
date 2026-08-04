'''
The problem statement for reversing a stack is:

Given a stack of integers, reverse the order of its elements.
After reversing, the top element of the original stack becomes the bottom element of the reversed stack, and vice versa.
The operation should be performed using stack-based logic, without converting it into another data structure such as a list or queue.
Example:

Input stack: [1, 2, 3, 4, 5]
Output stack: [5, 4, 3, 2, 1]
'''
class Solution:
    def reversestack(self,stack:list[int]) ->list[int]:
        right,left = 0,len(stack)-1

        while(right<left):
            stack[right],stack[left] = stack[left],stack[right]

            right +=1
            left -=1

        return stack

stack = [1,2,3,4,5]
object = Solution()
print(object.reversestack(stack))


'''
Time Complexity:O(n)
Space Complexity:O(1)

'''


