
# tabu 

prime = int(1e9 + 7)

# Function to count distinct subsequences of s1 that match s2
def subsequenceCounting(s1, s2, n, m):
    # Initialize a DP table to store the count of distinct subsequences
    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    # Base case: There is exactly one subsequence of an empty string s2 in s1
    for i in range(n + 1):
        dp[i][0] = 1

    # Initialize dp[0][i] to 0 for i > 0 since an empty s1 cannot have a non-empty subsequence of s2
    for i in range(1, m + 1):
        dp[0][i] = 0

    # Fill in the DP table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the current characters match, we have two choices:
            # 1. Include the current character in both s1 and s2 (dp[i-1][j-1])
            # 2. Skip the current character in s1 (dp[i-1][j])
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % prime if s1[i - 1] == s2[j - 1] else dp[i - 1][j]

    # The final value in dp[n][m] is the count of distinct subsequences
    return dp[n][m]

def main():
    s1 = "babgbag"
    s2 = "bag"
    
    # Calculate and print the count of distinct subsequences
    print("The Count of Distinct Subsequences is", subsequenceCounting(s1, s2, len(s1), len(s2)))

if __name__ == "__main__":
    main()

