def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill the DP table
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # Length of LCS
    len_ = dp[n][m]
    # print(len_)    
    print()
    
    # Construct the LCS string
    i, j = n, m
    lcs_str = [""] * len_
    index = len_ - 1

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_str[index] = s1[i - 1]  # Store character
            index -= 1
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("The Longest Common Subsequence is", "".join(lcs_str))

def main():
    s1 = "abcde"
    s2 = "bdgek"
    lcs(s1, s2)

if __name__ == "__main__":
    main()
