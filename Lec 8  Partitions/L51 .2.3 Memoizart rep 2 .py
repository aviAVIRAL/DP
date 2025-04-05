
# meme  aso rep 

def f(i, j, arr, dp):
    if i > j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    maxi = float('-inf')
    for ind in range(i, j + 1):
        cost = a[i - 1] * a[ind] * a[j + 1] + f(i, ind - 1, arr, dp) + f(ind + 1, j, arr, dp)
        maxi = max(maxi, cost)
    dp[i][j] = maxi
    return maxi

def maxCoins(arr):
    n = len(arr)
    arr.insert(0, 1)
    arr.append(1)

    dp = [[-1] * (n + 2) for _ in range(n + 2)]

    return f(1, n,   arr , dp )

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)



