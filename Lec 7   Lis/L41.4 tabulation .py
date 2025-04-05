
# tabulation  striver 

def lis_tabulation(arr):
    n = len(arr)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for ind in range(n - 1, -1, -1):
        for PrevIndx in range(ind - 1, -2, -1):
            len1 = dp[ind + 1][PrevIndx + 1]  # not take
            
            if PrevIndx == -1 or arr[ind] > arr[PrevIndx]:  # take
                len1 = max(len1, 1 + dp[ind + 1][ind + 1])
            
            dp[ind][PrevIndx + 1] = len1
    
    return dp[0][-1  + 1 ]
    return dp[0][0]

if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis_tabulation(arr))
