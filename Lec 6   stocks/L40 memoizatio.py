


# Buy and Sell Stocks With Transaction Fee|(DP-40) 

# memoization  

def get_max_profit(prices, ind, buy, n, fee, dp):
    # Base case: if we reach the end of the array
    if ind == n:
        return 0

    # Check if the result is already calculated
    if dp[ind][buy] != -1:
        return dp[ind][buy]

    profit = 0

    if buy == 0:  # We can buy the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 0, n, fee, dp),
            -prices[ind] + get_max_profit(prices, ind + 1, 1, n, fee, dp)
        )

    if buy == 1:  # We can sell the stock
        profit = max(
            0 + get_max_profit(prices, ind + 1, 1, n, fee, dp),
            prices[ind] - fee + get_max_profit(prices, ind + 1, 0, n, fee, dp)
        )

    dp[ind][buy] = profit
    return profit


def maximum_profit(n, fee, prices):
    dp = [[-1 for _ in range(2)] for _ in range(n)]

    if n == 0:
        return 0

    ans = get_max_profit(prices, 0, 0, n, fee, dp)
    return ans


if __name__ == "__main__":
    prices = [1, 3, 2, 8, 4, 9]
    n = len(prices)
    fee = 2

    result = maximum_profit(n, fee, prices)
    print(f"The maximum profit that can be generated is {result}")


