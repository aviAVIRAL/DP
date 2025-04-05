
# Buy and Sell Stock - IV | (DP - 38) 



def get_max_profit(prices, n, ind, buy, cap, dp):
    # Base case: if we reach the end of the array or have no more capital left
    if ind == n or cap == 0:
        return 0

    # Check if the result is already calculated
    if dp[ind][buy][cap] != -1:
        return dp[ind][buy][cap]

    # Initialize profit
    profit = 0

    if buy == 0:  # We can buy the stock
        profit = max(
            0 + get_max_profit(prices, n, ind + 1, 0, cap, dp),
            -prices[ind] + get_max_profit(prices, n, ind + 1, 1, cap, dp)
        )

    if buy == 1:  # We can sell the stock
        profit = max(
            0 + get_max_profit(prices, n, ind + 1, 1, cap, dp),
            prices[ind] + get_max_profit(prices, n, ind + 1, 0, cap - 1, dp)
        )

    # Memoize the result and return
    dp[ind][buy][cap] = profit
    return profit


def maximum_profit(prices, n, k):
    # Creating a 3D dp array of size [n][2][k+1]
    dp = [[[(-1) for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]

    return get_max_profit(prices, n, 0, 0, k, dp)


if __name__ == "__main__":
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    n = len(prices)
    k = 2

    result = maximum_profit(prices, n, k)
    print(f"The maximum profit that can be generated is {result}")




