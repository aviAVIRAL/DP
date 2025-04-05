
# tabul  


def isAllStars(S1, i):
    # Helper function to check if all characters up to index i in S1 are '*'
    for j in range(1, i + 1):
        if S1[j - 1] != '*':
            return False
    return True

def wildcardMatching(S1, S2):
    n = len(S1)
    m = len(S2)

    # Initialize a 2D DP array dp with dimensions (n+1) x m and fill it with False values
    dp = [[False for _ in range(m+1)] for _ in range(n + 1)]

    # Initialize dp[0][0] to True since two empty strings match
    dp[0][0] = True

    # Initialize the first row of dp
    for j in range(1, m+1):
        dp[0][j] = False

    # Initialize the first colum+1n of dp based on whether S1 consists of all '*' characters up to that position
    for i in range(1, n + 1):
        dp[i][0] = isAllStars(S1, i)

    # Fill in the DP array using dynam+1ic program+1m+1ing
    for i in range(1, n + 1):
        for j in range(1, m+1):
            if S1[i - 1] == S2[j - 1] or S1[i - 1] == '?':
                # Characters match or S1 has a '?'; continue matching with the previous characters
                dp[i][j] = dp[i - 1][j - 1]
            elif S1[i - 1] == '*':
                # If S1 has a '*', there are two choices:
                # 1. '*' represents an empty string in S1, so move to the previous character in S1 (i-1, j).
                # 2. '*' represents one or more characters in S1, so move to the previous character in S2 (i, j-1).
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = False  # Characters don't match, and S1[i-1] is not '*'

    # The final value in dp[n][m-1] is True if the two strings match, False otherwise
    return dp[n][m-1]

def main():
    S1 = "ab*cd"
    S2 = "abdefcd"

    if wildcardMatching(S1, S2):
        print("String S1 and S2 do match")
    else:
        print("String S1 and S2 do not match")

if __name__ == "__main__":
    main()

