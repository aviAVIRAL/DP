

# memeoization 

import sys

def f(arr, i, j, dp):
    # Base condition
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mini = sys.maxsize

    # Partitioning loop
    for k in range(i, j):
        ans = f(arr, i, k, dp) + f(arr, k + 1, j, dp) + arr[i - 1] * arr[k] * arr[j]
        mini = min(mini, ans)

    dp[i][j] = mini
    return dp[i][j]

def matrixMultiplication(arr, N):
    dp = [[-1] * N for _ in range(N)]  # Initialize DP table with -1
    return f(arr, 1, N - 1, dp)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    print("The minimum number of operations is", matrixMultiplication(arr, n))






