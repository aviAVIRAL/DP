

# unique optimize solution ALSORITHUM COS E SOLUTION 

def lis_bottom_up(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with 1
    maxi = 1  # Stores the maximum LIS found

    for ind in range(n):
        for prev in range(ind):
            if arr[prev] < arr[ind]:  # Valid LIS condition
                dp[ind] = max(dp[ind], 1 + dp[prev])  # Update DP value

        maxi = max(maxi, dp[ind])  # Track maximum LIS found

    return maxi

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis_bottom_up(arr))





