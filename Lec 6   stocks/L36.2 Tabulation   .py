

# striver tabulation  
#   0  not buy    
#   1   buy 

def getMaximumProfit(Arr, n):
    dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    print()
    print(dp)
    print()
    dp[n][0] = dp[n][1] = 0
    
    for i in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            
            if buy == 1:
                profit = max(0 + dp[i + 1][1], -Arr[i] + dp[i + 1][0])
            else:
                profit = max(0 + dp[i + 1][0], Arr[i] + dp[i + 1][1])
            
            dp[i][buy] = profit
    print(dp)          
    return dp[0][1]

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]
    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


