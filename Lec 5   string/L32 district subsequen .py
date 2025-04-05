

# memo

def f(s1, s2, i, j, dp):
    if j < 0:return 1
    if i < 0: return 0
    if dp[i][j] != -1:return dp[i][j]
    if s1[i] == s2[j]:
        dp[i][j] = f(s1, s2, i - 1, j - 1, dp) +f(s1, s2, i - 1, j, dp) # % prime
        return dp[i][j]
    else:
        dp[i][j] = f(s1, s2, i - 1, j, dp)
        return dp[i][j]

if __name__ == "__main__":
    s1 = "babgbag"
    s2 = "bag"
    n = len(s1)
    m = len(s2)
    dp = [[-1 for j in range(m)] for i in range(n)]
    print( f(s1, s2, n - 1, m - 1, dp))


