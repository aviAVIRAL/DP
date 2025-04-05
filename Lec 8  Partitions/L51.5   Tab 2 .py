


def maxCoins(a):
    n = len(a)
    a.insert(0, 1)
    a.append(1)

    # Create a 2D DP table initialized with zeros
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # Calculate the maximum coins using dynamic programming
    for length in range(1, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            maxi = float('-inf')
            
            for ind in range(i, j + 1):
                cost = a[i - 1] * a[ind] * a[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                maxi = max(maxi, cost)
            
            dp[i][j] = maxi
    
    return dp[1][n]

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)
