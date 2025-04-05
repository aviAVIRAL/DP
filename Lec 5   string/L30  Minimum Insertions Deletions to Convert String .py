



def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize a 2D array to store the length of the LCS
    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    # Base cases: When one of the strings is empty, LCS length is 0.
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # Fill in the dp array using dynamic programming
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # The final value in dp will be the length of the LCS
    return dp[n][m]

# Function to calculate the minimum operations required to convert str1 to str2
def canYouMake(str1, str2):
    n = len(str1)
    m = len(str2)

    # Calculate the length of the LCS between str1 and str2
    k = lcs(str1, str2)

    # The minimum operations required is the sum of the deletions needed in both strings
    return (n - k) + (m - k)

def main():
    str1 = "abcd"
    str2 = "anc"

    # Calculate and print the minimum operations required to convert str1 to str2
    print("The Minimum operations required to convert str1 to str2:", canYouMake(str1, str2))

if __name__ == '__main__':
    main()



