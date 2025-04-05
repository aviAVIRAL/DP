# also rep 


def max_sum_after_partitioning(num, k):
    n = len(num)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        max_val = 0
        for j in range(1, min(i, k) + 1):
            max_val = max(max_val, num[i - j])
            dp[i] = max(dp[i], dp[i - j] + max_val * j)

    return dp[n]

if __name__ == "__main__":
    num = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    max_sum = max_sum_after_partitioning(num, k)
    print("The maximum sum is:", max_sum)