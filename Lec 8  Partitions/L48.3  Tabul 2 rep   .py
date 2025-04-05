# tabulation  
# striver rep 
def matrix_multiplication(arr, N):
    dp = [[-1] * N for _ in range(N)]

    for i in range(N):
        dp[i][i] = 0

    for i in range(n-1 , -1, -1 ):
        for j in range(i+1, n ):
            dp[i][j] = int(1e7)  # Equivalent to INT_MAX

            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)

    return dp[1][N - 1]

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    n = len(arr)
    print("The ix multiplication is", matrix_multiplication(arr, n))

# aslo rep re  

    # for i in range(n-1 , -1, -1 ):
    #     for j in range(i+1, n ):

    #         mini = int(1e7)                  # see repre also 

    #         for k in range(i, j):
    #             Steps = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
    #             mini = min(mini , Steps)     # see repre also
    #             dp[i][j] = mini              # see repre also

    # return dp[1][N - 1]
