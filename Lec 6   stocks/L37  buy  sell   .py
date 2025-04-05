
# Buy and Sell Stock - III | (DP - 37) 


# meemo ization

def maxProfit(prices):
    n = len(prices)
    
    # Create a 3D DP table with dimensions (n) x 2 x 3 and initialize it with -1 values
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
    
    def getAns(ind, buy, cap):
        # Recursive function to calculate the maximum profit
        
        if ind == n or cap == 0:
            return 0  # Base case: If we have reached the end of the array or used up all transactions, return zero profit
        
        if dp[ind][buy][cap] != -1:
            return dp[ind][buy][cap]  # If the result is already computed, return it
        
        profit = 0
        
        if buy == 0:
            # We can buy the stock
            profit = max(0 + getAns(ind + 1, 0, cap), -prices[ind] + getAns(ind + 1, 1, cap))
        elif buy == 1:
            # We can sell the stock
            profit = max(0 + getAns(ind + 1, 1, cap), prices[ind] + getAns(ind + 1, 0, cap - 1))
        
        dp[ind][buy][cap] = profit  # Store the result in the DP table
        return profit

    return getAns(0, 0, 2)  # Start with buying (0) and 2 transactions available (cap=2)

def main():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]

    max_profit = maxProfit(prices)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()




