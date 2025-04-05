 

# rep     nested funtion  

def maxCoins(a):
    n = len(a)
    # Extend the list 'a' with 1s at both ends
    a.insert(0, 1)
    a.append(1)

    # Create a 2D DP table initialized with -1s
    dp = [[-1] * (n + 2) for _ in range(n + 2)]

# --------------------------------
    def f(i, j):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi = float('-inf')
        for ind in range(i, j + 1):
            cost = a[i - 1] * a[ind] * a[j + 1] + f(i, ind - 1) + f(ind + 1, j)
            maxi = max(maxi, cost)
        dp[i][j] = maxi
        return maxi
# --------------------------------

    return f(1, n)

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)


