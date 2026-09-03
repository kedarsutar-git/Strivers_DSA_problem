'''

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
        candidate = stack.pop()
        
        # Step 4: Verify candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know anyone
                if M[candidate][i] == 1:
                    return -1
                # Everyone should know candidate
                if M[i][candidate] == 0:
                    return -1
        
        return candidate


# Example usage:
M = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
n = 3

sol = Solution()
print(sol.celebrity(M, n))  # Output: 1 (Person 1 is celebrity)
