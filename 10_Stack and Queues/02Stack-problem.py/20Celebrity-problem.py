'''
Example 1:
Input:
 M = [ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]
Output:
 1
Explanation:
 Person 1 does not know anyone and is known by persons 0, 2, and 3. Therefore, person 1 is the celebrity.

Example 2:
Input:
 M = [ [0, 1], [1, 0] ]
Output:
 -1
Explanation:
 Both persons know each other, so there is no celebrity.

'''


class Solution:
    def celebrity(self, M, n):
        # Step 1: Push all people into stack
        stack = [i for i in range(n)]
        
        # Step 2: Eliminate candidates
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            if M[a][b] == 1:
                # a knows b → a cannot be celebrity
                stack.append(b)
            else:
                # a does not know b → b cannot be celebrity
                stack.append(a)
        
        # Step 3: Potential celebrity
        celebrity = stack.pop()
        
        # Step 4: Verify candidate
        for i in range(n):
            if i != celebrity:
                # Candidate should not know anyone
                if M[celebrity][i] == 1:
                    return -1
                # Everyone should know candidate
                if M[i][celebrity] == 0:
                    return -1
        
        return celebrity


# Example usage:
M = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
n = 3

sol = Solution()
print(sol.celebrity(M, n))  # Output: 1 (Person 1 is celebrity)
