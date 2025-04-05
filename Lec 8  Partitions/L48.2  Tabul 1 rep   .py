# tabulation  

import sys

def matrix_multiplication(arr, N):
    # Create a DP table to store the minimum number of operations
    dp = [[-1] * N for _ in range(N)]

    # Initialize the diagonal elements of the DP table to 0
    for i in range(N):
        dp[i][i] = 0

    # Loop for the length of the chain
    for length in range(2, N):
        for i in range(1, N - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize  # Equivalent to INT_MAX

            # Try different partition points to find the minimum
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)

    # The result is stored in dp[1][N-1]
    return dp[1][N - 1]

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)

    print("The minimum number of operations for matrix multiplication is", matrix_multiplication(arr, n))
