# tabulatiomnn  

# TAULAT

def countWaysUtil(m, n, dp):
    # Loop through each cell in the grid
    for i in range(m):
        for j in range(n):
            # Base condition: If we are at the top-left corner, there is one way to reach it.
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            
            # Initialize variables to store the number of ways from above and from the left.
            up = 0
            left = 0
            
            # Check if moving up is a valid option (not out of bounds).
            if i > 0:
                up = dp[i - 1][j]
            
            # Check if moving left is a valid option (not out of bounds).
            if j > 0:
                left = dp[i][j - 1]
            
            # Calculate and store the number of ways to reach the current cell.
            dp[i][j] = up + left
    
    # The bottom-right cell (m-1, n-1) now contains the total number of ways to reach there.
    return dp[m - 1][n - 1]

def countWays(m, n):
    # Initialize a memoization (dp) array to store intermediate results.
    dp = [[-1 for j in range(n)] for i in range(m)]
    
    # Call the utility function to compute the number of ways to reach the destination.
    return countWaysUtil(m, n, dp)

def main():
    m = 3
    n = 2
    # Call the countWays function to calculate and print the number of ways to reach the destination.
    print(countWays(m, n))

if __name__ == '__main__':
    main()


# aslo repr as 

def countWaysUtil(m, n, dp):
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            else:
                up = 0 
                left = 0              
                if i > 0: up = dp[i - 1][j]
                if j > 0: left = dp[i][j - 1]
                
                dp[i][j] = up + left

    return dp[m - 1][n - 1]

def countWays(m, n):
    dp = [[-1 for j in range(n)] for i in range(m)]
    return countWaysUtil(m, n, dp)

def main():
    m = 3
    n = 2
    print(countWays(m, n))

if __name__ == '__main__':
    main()

