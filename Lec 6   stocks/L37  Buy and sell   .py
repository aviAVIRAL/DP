

# tabulatio 

def maxProfit(prices):
    n = len(prices)
    
    # Create a 3D DP table with dimensions (n+1) x 2 x 3 and initialize it to 0 values
    dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n + 1)]
    print(dp)
    
    # The base case is already covered as the DP array is initialized to 0
    
    for ind in range(n - 1, -1, -1):
        for buy in range(2):
            for cap in range(1,3):
                
                if buy:
                    # We can buy the stock
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][1][cap], -prices[ind] + dp[ind + 1][0][cap])
                else:
                    # We can sell the stock
                    dp[ind][buy][cap] = max(0 + dp[ind + 1][0][cap], prices[ind] + dp[ind + 1][1][cap - 1])
    
    print()
    print(dp)
    print()
    return dp[0][1][2] #

def main():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    max_profit = maxProfit(prices)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


[[[0, 5, 9], [0, 4, 6]], 
 [[0, 5, 9], [0, 4, 6]], 
 [[0, 5, 9], [0, 4, 6]],
   [[0, 4, 6], [0, 4, 6]],
     [[0, 4, 6], [0, 4, 6]],
       [[0, 4, 6], [0, 3, 3]],
         [[0, 4, 4], [0, 3, 3]],
           [[0, 4, 4], [0, 0, 0]],
             [[0, 0, 0], [0, 0, 0]]] 






