

# mem 

import sys

# Recursive function to find the maximum chocolates collected
def maxChocoUtil(i, j1, j2, n, m, grid, dp):
    # Base cases:
    # - If either of the indices is out of bounds, return a large negative value
    # - If we're at the last row, return the sum of chocolates in the two selected columns
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return int(-1e9)  # -10**8  
    if i == n - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
    
    # If the result for these indices has already been computed, return it
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]
    
    # Initialize the maximum chocolates collected to a large negative value
    maxi = -sys.maxsize
    
    # Iterate through the adjacent cells in the next row
    for di in range(-1, 2):
        for dj in range(-1, 2):
            # ans = 0
            if j1 == j2:
                maxi = max(maxi, grid[i][j1] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp))
            else:
                maxi = max(maxi , grid[i][j1] + grid[i][j2] + maxChocoUtil(i + 1, j1 + di, j2 + dj, n, m, grid, dp))
            # maxi = max(maxi, ans)
    
    # Store the maximum chocolates collected in the memoization table
    dp[i][j1][j2] = maxi
    return maxi

# Function to find the maximum chocolates collected
def maximumChocolates(n, m, grid):
    # Initialize a memoization table with -1 values
    dp = [[[-1 for j in range(m)] for i in range(m)] for k in range(n)]
    dp = [[[-1 ]*m  for i in range(m)] for k in range(n)]
    print(dp)
    print()
    # Start the recursion from the first row, columns 0 and m-1
    return maxChocoUtil(0, 0, m - 1, n, m, grid, dp)

def main():
    # Define the input matrix and its dimensions
    matrix = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
    n = len(matrix)
    m = len(matrix[0])
    
    # Call the maximumChocolates function and print the result
    print(maximumChocolates(n, m, matrix))

if __name__ == "__main__":
    main()


