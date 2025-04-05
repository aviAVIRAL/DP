
# tabualktiion   

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table with dimensions (n+1) x (m+1) initialized to zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Initialize a variable 'ans' to keep track of the maximum LCS length
    ans = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j]  = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j] )
            else:
                dp[i][j] = 0
    
    return ans

def main():
    s1 = "abcjklp"
    s2 = "acjkp"

    print("The Length of Longest Common Substring is", lcs(s1, s2))

if __name__ == '__main__':
    main()
