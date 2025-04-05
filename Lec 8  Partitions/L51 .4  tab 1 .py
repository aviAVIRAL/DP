

def maxCoins(a):
    n = len(a)
    
    # Extend the list 'a' with 1s at both ends
    a.insert(0, 1)
    a.append(1)

    # Create a 2D DP table initialized with 0s
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # Loop from the end of 'a' to the beginning
    for i in range(n, 0, -1):
        for j in range(1, n + 1):
            if i > j:
                continue
            maxi = float('-inf')
            
            # Iterate through the balloons from 'i' to 'j'
            for ind in range(i, j + 1):
                cost = a[i - 1] * a[ind] * a[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                maxi = max(maxi, cost)
            
            dp[i][j] = maxi
    
    return dp[1][n]

if __name__ == "__main__":
    a = [3, 1, 5, 8]
    ans = maxCoins(a)
    print(ans)


