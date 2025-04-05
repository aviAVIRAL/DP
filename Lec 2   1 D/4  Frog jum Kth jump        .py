
# memo 


# Recursive function to calculate the minimum cost to reach the end
# from a given index with at most 'k' jumps.
def solveUtil(ind, height, dp, k):
    # Base case: If we are at the beginning (index 0), no cost is needed.
    if ind == 0:
        return 0
    # If the result for this index has been previously calculated, return it.
    if dp[ind] != -1:
        return dp[ind]

    mmSteps = 10000

    # Loop to try all possible jumps from '1' to 'k'
    for j in range(1, k + 1):
        # Ensure that we do not jump beyond the beginning of the array
        if ind - j >= 0:
            # Calculate the cost for this jump and update mmSteps with the minimum cost
            jump = solveUtil(ind - j, height, dp, k) + abs(height[ind] - height[ind - j])
            mmSteps = min(jump, mmSteps)

    # Store the minimum cost for this index in the dp array and return it.
    dp[ind] = mmSteps
    return dp[ind]

# Function to find the minimum cost to reach the end of the array
def solve(n, height, k):
    dp = [-1] * n  # Initialize a memoization array to store calculated results
    return solveUtil(n - 1, height, dp, k)  # Start the recursion from the last index

def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2 # impo see  foolloklmikkdf fv f nwijeuhyvb   jk dfbnhmhxd  
    print(solve(n, height, k))  # Print the result of the solve function

if __name__ == "__main__":
    main()


# tabulation    

import sys

# Helper function to solve the problem using dynamic programming
def solve_util(n, height, dp, k):
    # Initialize the first element of the dp array as 0 since no steps are needed to reach the first position
    dp[0] = 0

    # Loop through the elements of the height array
    for i in range(1, n):
        mmSteps = sys.maxsize  # Initialize the minimum steps to a large value
        for j in range(1, k+1):
            if i - j >= 0:
                # Calculate the number of steps required to reach the current position from the previous positions
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)  # Update the minimum steps
        dp[i] = mmSteps  # Store the minimum steps needed to reach the current position

    return dp[n-1]  # Return the minimum steps needed to reach the last position

# Main function to solve the problem
def solve(n, height, k):
    dp = [-sys.maxsize] * n  # Initialize a dp array with large negative values
    return solve_util(n, height, dp, k)  # Call the helper function

# Entry point of the program
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    dp = [-sys.maxsize] * n  # Initialize dp array
    result = solve(n, height, k)  # Call the solve function
    print(result)  # Print the result

if __name__ == "__main__":
    main()


