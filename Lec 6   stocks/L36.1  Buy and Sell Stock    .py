
# memeoization

# notes repre   0 : buy 
#   and         1 : not buy 

def getMaximumProfit(Arr, n):
    # Function to calculate the maximum profit from buying and selling stocks
    
    if n == 0:
        return 0  # If there are no stocks, the profit is zero

    dp = [[-1 for _ in range(2)] for _ in range(n)]  # Initialize a DP table with -1 values

    def getAns(ind, buy):
        # Recursive function to calculate the maximum profit
        
        if ind == n:
            return 0  # Base case: If we have reached the end of the array, return zero profit
        
        if dp[ind][buy] != -1:
            return dp[ind][buy]  # If the result is already computed, return it
        
        profit = 0
        
        if buy == 0:
            # We can buy the stock
            profit = max(0 + getAns(ind + 1, 0), -Arr[ind] + getAns(ind + 1, 1))
        elif buy == 1:
            # We can sell the stock
            profit = max(0 + getAns(ind + 1, 1), Arr[ind] + getAns(ind + 1, 0))
        
        dp[ind][buy] = profit  # Store the result in the DP table
        return profit

    ans = getAns(0, 0)  # Start with buying (0) at the first day (0)
    return ans

def main():
    n = 6
    Arr = [7, 1, 5, 3, 6, 4]

    max_profit = getMaximumProfit(Arr, n)
    print("The maximum profit that can be generated is", max_profit)

if __name__ == "__main__":
    main()


