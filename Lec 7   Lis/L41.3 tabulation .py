# tabul  framwork 

def lis_tabulation(arr):
    n = len(arr)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for ind in range(n - 1, -1, -1):
        for prev_index in range(ind - 1, -2, -1):
            not_take = dp[ind + 1][prev_index + 1]  # Not take case
            take = 0
            
            if prev_index == -1 or arr[ind] > arr[prev_index]:  # Take case
                take = 1 + dp[ind + 1][ind + 1]
            
            dp[ind][prev_index + 1] = max(not_take, take)
    
    return dp[0][0] 

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis_tabulation(arr))
