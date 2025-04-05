
# rep  1 is not buy  but 0 is buy 

def getMaximumProfit(Arr, n):
    dp = [[-1 for _ in range(2)] for _ in range(n + 1)]
    dp[n][0] = dp[n][1] = 0
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            profit = 0
            if buy == 0:
                # We can buy the stock
                profit = max(0 + dp[ind + 1][0], -Arr[ind] + dp[ind + 1][1])
            elif buy == 1:
                # We can sell the stock
                profit = max(0 + dp[ind + 1][1], Arr[ind] + dp[ind + 1][0])
            
            dp[ind][buy] = profit  #
    
    return dp[0][0] # immport

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


