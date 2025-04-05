


def countWaysUtil(i, j, dp):
    # Base case: If we reach the top-left corner (i=0, j=0), there is one way to reach there.
    if i == 0 and j == 0:
        return 1
    # If either i or j goes out of bounds (negative), there is no way to reach that cell.
    if i < 0 or j < 0:
        return 0
    # If we have already calculated the number of ways for this cell, return it from the dp array.
    if dp[i][j] != -1:
        return dp[i][j]
    
    # Recursive calls to count the number of ways to reach the current cell.
    up = countWaysUtil(i - 1, j, dp)    # Moving up one row.
    left = countWaysUtil(i, j - 1, dp)  # Moving left one column.
    
    # Store the result in the dp array and return it.
    dp[i][j] = up + left
    return dp[i][j]

def countWays(m, n):
    # Initialize a memoization (dp) array to store intermediate results.
    dp = [[-1 for j in range(n)] for i in range(m)]
    
    # Call the utility function to compute the number of ways to reach the bottom-right cell (m-1, n-1).
    return countWaysUtil(m - 1, n - 1, dp)

def main():
    m = 3
    n = 2
    # Call the countWays function to calculate and print the number of ways to reach the destination.
    print(countWays(m, n))

if __name__ == '__main__':
    main()

