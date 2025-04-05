# Buy and Sell Stocks With Cooldown | (DP - 39)

# memeo  

def get_max_profit(prices, ind, buy, n, dp):
    # Base case: if we reach the end of the array
    if ind >= n:
        return 0

    # Check if the result is already calculated
    if dp[ind][buy] != -1:
        return dp[ind][buy]

    # Initialize profit
    profit = 0

    if buy == 0:  # We can buy the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 0, n, dp),
            -prices[ind] + get_max_profit(prices, ind + 1, 1, n, dp)
        )

    if buy == 1:  # We can sell the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 1, n, dp),
            prices[ind] + get_max_profit(prices, ind + 2, 0, n, dp)
        )

    # Memoize the result and return
    dp[ind][buy] = profit
    return profit


def stock_profit(prices):
    n = len(prices)
    dp = [[-1 for _ in range(2)] for _ in range(n)]

    ans = get_max_profit(prices, 0, 0, n, dp)
    return ans


if __name__ == "__main__":
    prices = [4, 9, 0, 4, 10]

    result = stock_profit(prices)
    print(f"The maximum profit that can be generated is {result}")


